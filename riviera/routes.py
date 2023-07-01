from flask import render_template, url_for, request, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from io import BytesIO
import base64
import pandas as pd
from matplotlib.figure import Figure
import uuid
from yookassa import Configuration, Payment

from riviera import application, db
from riviera.models import Users, Profiles, Utilities, Service, Payments, Houses, Texts, News, Feedbacks
from riviera.forms import LoginForm, RegisterForm, SendUtility, SendPayment, FeedbackForm


@application.route('/index')
@application.route('/')
def index():

    texts = db.session.execute(db.select(Texts).filter_by(label='index')).scalars().all()
    return render_template('index.html', texts=texts)


@application.route('/news')
def news():

    news_db = db.session.execute(db.select(News)).scalars().all()
    return render_template('news.html', news=news_db)


@application.route('/houses', methods=['POST', 'GET'])
def houses():

    description = db.session.execute(db.select(Texts).filter_by(label='houses')).scalars().all()
    houses_pay = db.session.execute(db.select(Houses)).scalars().all()
    price_zx83 = '{:,}'.format(houses_pay[0].price)
    price_zx149 = '{:,}'.format(houses_pay[1].price)
    price_zx153 = '{:,}'.format(houses_pay[2].price)
    price_zx101 = '{:,}'.format(houses_pay[3].price)
    path_zx83 = tuple(f'images/zx83/{i}.png' for i in range(1, 6))
    path_zx149 = tuple(f'images/zx149/{i}.png' for i in range(1, 6))
    path_zx153 = tuple(f'images/zx153/{i}.png' for i in range(1, 6))
    path_zx101 = tuple(f'images/zx101/{i}.png' for i in range(1, 6))

    form_feedback = FeedbackForm()

    if form_feedback.validate_on_submit():

        feedback = Feedbacks(name=form_feedback.name.data, tel=form_feedback.tel.data)
        db.session.add(feedback)
        db.session.commit()

        if feedback:
            flash('Заявка отправлена', 'feedback_success')
            return redirect(url_for('houses', _anchor='feedback'))
        else:
            flash('Заявка не отправлена', 'feedback_danger')

    return render_template('houses.html', houses=houses_pay, price_zx83=price_zx83, price_zx149=price_zx149,
                           price_zx153=price_zx153, price_zx101=price_zx101, path_zx83=path_zx83,
                           path_zx149=path_zx149, path_zx153=path_zx153, path_zx101=path_zx101,
                           description=description, form=form_feedback)


@application.route('/login', methods=['POST', 'GET'])
def login_page():

    if current_user.is_authenticated:
        return redirect(url_for('owner'))

    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.execute(db.select(Users).filter_by(login=form.login.data)).scalar()

        if user and check_password_hash(user.password, form.password.data):
            check = form.remember.data
            login_user(user, remember=check)
            return redirect(request.args.get('next') or url_for('owner'))
        else:
            flash('Неправильное имя пользователя и/или пароль', 'login_danger')

    return render_template('login.html', title='Авторизация', form=form)


@application.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():

    logout_user()
    return redirect(url_for('index'))


@application.route('/register', methods=['POST', 'GET'])
def register():

    form_reg = RegisterForm()

    if form_reg.validate_on_submit():

        hash_password = generate_password_hash(form_reg.password.data)
        user = Users(login=form_reg.login.data, password=hash_password, date=datetime.utcnow())

        db.session.add(user)
        db.session.flush()

        profile = Profiles(name=form_reg.name.data, tel=form_reg.tel.data, email=form_reg.email.data,
                           address=form_reg.address.data, balance=0, account=user.id, user_id=user.id)

        db.session.add(profile)
        db.session.flush()

        utility = Utilities(date=datetime.utcnow(), value_electro=0, value_gas=0, value_water=0,
                            summ=0, user_id=user.id)

        db.session.add(utility)
        db.session.commit()

        if all([user, profile, utility]):

            flash('Вы успешно зарегистрированы. Авторизуйтесь', 'register_success')
            return redirect(request.args.get('next') or url_for('login_page'))
        else:
            flash('Ошибка при регистрации', 'register_danger')

    return render_template('register.html', title='Авторизация', form=form_reg)


@application.route('/owner', methods=['POST', 'GET'])
@login_required
def owner():

    """ Secret Key и ID тестового 'магазина' для приема платежей по Ю-Кассе """
    Configuration.account_id = '221121'
    Configuration.secret_key = 'test_ncmxV6aAcu96URvfWIjUo2brCBAPB6wybqWMYi-ilWo'

    profile = db.session.execute(db.select(Profiles).filter_by(user_id=current_user.id)).scalar()
    utility = db.session.execute(db.select(Utilities).filter_by(user_id=current_user.id)).scalars().all()
    payments = db.session.execute(db.select(Payments).filter_by(user_id=current_user.id)).scalars().all()
    service = db.session.execute(db.select(Service)).scalars().all()

    print('сюда зашли')
    for payment in payments:
        payment_id = Payment.find_one(payment.payment_id)  # запрос о платеже в "Юкассу"
        if payment_id.status == 'succeeded':
            payment.status = True
            db.session.commit()

    payments_summ = sum([int(i.payment_summ) for i in payments if i.status])
    utility_summ = sum(int(i.summ) for i in utility)
    profile.balance = payments_summ - utility_summ
    db.session.commit()

    form_utility = SendUtility(user=current_user.id)

    if form_utility.validate_on_submit():

        value_electro = form_utility.electro.data
        value_gas = form_utility.gas.data
        value_water = form_utility.water.data

        summ = (int(value_electro) - utility[-1].value_electro) * service[0].tariff / 100 + \
               (int(value_gas) - utility[-1].value_gas) * service[1].tariff / 100 + \
               (int(value_water) - utility[-1].value_water) * service[2].tariff / 100 + service[3].tariff / 100

        utility = Utilities(date=datetime.utcnow(), value_electro=value_electro, value_gas=value_gas,
                            value_water=value_water, summ=int(summ * 100), user_id=current_user.id)

        db.session.add(utility)
        db.session.commit()

        if utility:
            flash('Показания успешно переданы', 'utility_success')
            return redirect(request.args.get('next') or url_for('owner'))
        else:
            flash('Ошибка при передаче показаний', 'utility_danger')

    return render_template('owners.html', profile=profile, utility=utility, service=service,
                           form=form_utility)


@application.route('/history')
@login_required
def history():

    profile = db.session.execute(db.select(Profiles).filter_by(user_id=current_user.id)).scalar()
    payments = db.session.execute(db.select(Payments).filter_by(user_id=current_user.id)).scalars().all()
    utility = db.session.execute(db.select(Utilities).filter_by(user_id=current_user.id)).scalars().all()
    balance_sum = sum([int(i.payment_summ) for i in payments if i.status == 1])

    debet = pd.Series([(i.date, i.summ) for i in utility])
    kredit = pd.Series([(i.date, i.payment_summ) for i in payments if i.status == 1])
    df_debet = pd.DataFrame([int(i[1]) / 100 for i in debet], index=[i[0] for i in debet]).\
        rename(columns={0: 'debet'})

    if not kredit.empty:
        df_kredit = pd.DataFrame([int(i[1]) / 100 for i in kredit], index=[i[0] for i in kredit]).\
            rename(columns={0: 'kredit'})
        df = pd.concat([df_debet, df_kredit], axis=0).sort_index().fillna(0)
    else:
        df = df_debet
        df['kredit'] = pd.Series()
        df = df.fillna(0)
    df['balance'] = round(df.kredit.cumsum() - df.debet.cumsum(), 2)

    return render_template('history.html', utility=utility, profile=profile, balance_sum=balance_sum, df=df)


@application.route('/pay', methods=['POST', 'GET'])
@login_required
def pay():

    profile = db.session.execute(db.select(Profiles).filter_by(user_id=current_user.id)).scalar()
    utility = db.session.execute(db.select(Utilities).filter_by(user_id=current_user.id)).scalars().all()
    service = db.session.execute(db.select(Service)).scalars().all()

    form_payment = SendPayment(balance=profile.balance)

    if form_payment.validate_on_submit():
        summ = form_payment.payment.data
    else:
        return render_template('pay.html', form=form_payment, utility=utility, service=service)

    """ Secret Key и ID тестового 'магазина' для приема платежей по Ю-Кассе """
    Configuration.account_id = '221121'
    Configuration.secret_key = 'test_ncmxV6aAcu96URvfWIjUo2brCBAPB6wybqWMYi-ilWo'
    payment = Payment.create({
        "amount": {
            "value": summ,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://127.0.0.1:8000/owner"
        },
        "capture": True,
        "description": profile.user_id
    }, uuid.uuid4())

    payment_db = Payments(date=datetime.utcnow(), payment_id=payment.id, payment_summ=int(float(summ) * 100),
                          status=False, user_id=current_user.id)

    db.session.add(payment_db)
    db.session.commit()

    confirmation_url = payment.confirmation.confirmation_url
    return redirect(confirmation_url)


@application.route('/account', methods=['POST', 'GET'])
@login_required
def account():

    user = db.session.execute(db.select(Users.id).filter_by(id=current_user.id)).scalar()
    profile = db.session.execute(db.select(Profiles).filter_by(user_id=current_user.id)).scalar()
    utility = db.session.execute(db.select(Utilities).filter_by(user_id=current_user.id)).scalars().all()
    payments = db.session.execute(db.select(Payments).filter_by(user_id=current_user.id)).scalars().all()
    service = db.session.execute(db.select(Service)).scalars().all()

    form_utility = SendUtility(user=current_user.id)

    return render_template('account.html', user=user, profile=profile, utility=utility,
                           payments=payments, service=service, form=form_utility)


@application.route('/account/analytics', methods=['POST', 'GET'])
@login_required
def analytics():

    profile = db.session.execute(db.select(Profiles).filter_by(user_id=current_user.id)).scalar()
    utility = db.session.execute(db.select(Utilities).filter_by(user_id=current_user.id)).scalars().all()
    payments = db.session.execute(db.select(Payments).filter_by(user_id=current_user.id)).scalars().all()
    service = db.session.execute(db.select(Service)).scalars().all()

    flag = len(utility) > 1
    electro_value = []
    gas_value = []
    water_value = []

    if len(utility) <= 6:
        date = [i.date.strftime('%m-%Y') for i in utility][1:]

        for i in range(len(utility))[1:][::-1]:
            electro_value.append(utility[i].value_electro - utility[i - 1].value_electro)
            gas_value.append(utility[i].value_gas - utility[i - 1].value_gas)
            water_value.append(utility[i].value_water - utility[i - 1].value_water)
    else:
        date = [i.date.strftime('%m-%Y') for i in utility][-6:]

        for i in range(len(utility))[-6:][::-1]:
            electro_value.append(utility[i].value_electro - utility[i - 1].value_electro)
            gas_value.append(utility[i].value_gas - utility[i - 1].value_gas)
            water_value.append(utility[i].value_water - utility[i - 1].value_water)

    fig_electro = Figure()
    ax = fig_electro.subplots()
    ax.bar(date, tuple(reversed(electro_value)), width=0.5, color='orange')
    ax.tick_params(labelcolor='black', labelsize='small', width=3)
    buf_electro = BytesIO()
    fig_electro.savefig(buf_electro, format="svg")
    data_electro = base64.b64encode(buf_electro.getbuffer()).decode("ascii")

    fig_gas = Figure()
    ax = fig_gas.subplots()
    ax.bar(date, tuple(reversed(gas_value)), width=0.5, color='green')
    ax.tick_params(labelcolor='black', labelsize='small', width=3)
    buf_gas = BytesIO()
    fig_gas.savefig(buf_gas, format="svg")
    data_gas = base64.b64encode(buf_gas.getbuffer()).decode("ascii")

    fig_water = Figure()
    ax = fig_water.subplots()
    ax.bar(date, tuple(reversed(water_value)), width=0.5, color='blue')
    ax.tick_params(labelcolor='black', labelsize='small', width=3)
    buf_water = BytesIO()
    fig_water.savefig(buf_water, format="svg")
    data_water = base64.b64encode(buf_water.getbuffer()).decode("ascii")

    return render_template('analytics.html', profile=profile, utility=utility,
                           payments=payments, service=service, flag=flag,
                           data_electro=data_electro, data_gas=data_gas,
                           data_water=data_water)
