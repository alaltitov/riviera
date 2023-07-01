from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo, Regexp
from wtforms_validators import AlphaNumeric
from decimal import Decimal
from datetime import datetime

from riviera import db
from riviera.models import Users, Profiles, Utilities, Feedbacks


class LoginForm(FlaskForm):

    login = StringField(label='Имя пользователя',
                        validators=[Length(min=5, max=25,
                                           message=f'Имя пользователя должно быть не короче'
                                                   f' %(min)d и не длиннее %(max)d символов.'),
                                    DataRequired(message='Поле "Имя пользователя" не должно быть пустым'),
                                    AlphaNumeric(
                                        message='Поле "Имя пользователя должно состоять из букв и/или цифр"')],
                        render_kw={"placeholder": "Введите имя пользователя"})

    password = PasswordField(label='Пароль',
                             validators=[Length(min=3, max=25, message=f'Пароль должен быть не короче '
                                                                       f'%(min)d и не длиннее %(max)d символов.'),
                                         DataRequired(message='Поле "Пароль" не должно быть пустым')],
                             render_kw={"placeholder": "Введите пароль"})

    remember = BooleanField('запомнить', default=False)
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):

    login = StringField(label='Имя пользователя',
                        validators=[Length(min=5, max=25,
                                           message=f'Имя пользователя должно быть не короче'
                                                   f' %(min)d и не длиннее %(max)d символов.'),
                                    DataRequired(message='Поле "Имя пользователя" не должно быть пустым'),
                                    AlphaNumeric(message='Поле "Имя пользователя должно состоять из латинских букв и'
                                                         '/или цифр"')],
                        render_kw={"placeholder": "Введите имя пользователя"})

    password = PasswordField(label='Пароль',
                             validators=[Length(min=3, max=25, message=f'Пароль должен быть не короче '
                                                                       f'%(min)d и не длиннее %(max)d символов.'),
                                         DataRequired(message='Поле "Пароль" не должно быть пустым')],
                             render_kw={"placeholder": "Введите пароль"})

    password1 = PasswordField(label='Повторите пароль',
                              validators=[DataRequired(message='Поле "Пароль" не должно быть пустым'),
                                          EqualTo('password', message='Пароли не совпадают')],
                              render_kw={"placeholder": "Повторите пароль"})

    email = StringField(label='E-mail', validators=[Email("Некорректный e-mail")],
                        render_kw={"placeholder": "Введите e-mail"})

    pin = StringField(label='PIN', render_kw={"placeholder": "Введите PIN"})

    tel = StringField(label='Телефон',
                      validators=[Regexp(r'^\+7-\d{3}-\d{3}-\d{4}',
                                         message='Введите номер телефона в формате "+7-XXX-XXX-XXXX"')],
                      render_kw={"placeholder": "Введите номер телефона"})

    name = StringField(label='Фамилия, Имя',
                       validators=[DataRequired(message='Поле "Фамилия, Имя" не должно быть пустым')],
                       render_kw={"placeholder": "Введите Фамилию и Имя"})

    address = StringField(label='Адрес',
                          validators=[DataRequired(message='Поле "Адрес" не должно быть пустым')],
                          render_kw={"placeholder": "Введите адрес"})

    submit = SubmitField('Регистрация')

    def validate_pin(self, _):
        pin_validate = '123456'
        if pin_validate != self.pin.data:
            raise ValidationError("Введен неправильный PIN")

    def validate_login(self, _):
        temp = db.session.execute(db.select(Users.login))
        for i in temp:
            if i.login == self.login.data:
                raise ValidationError("Имя пользователя уже существует")

    def validate_email(self, _):
        temp = db.session.execute(db.select(Profiles.email))
        for i in temp:
            if i.email == self.email.data:
                raise ValidationError("Этот e-mail уже используется")


class SendUtility(FlaskForm):

    electro = StringField(label='Электроэнергия',
                          validators=[Length(min=1, max=7, message=f'Неверный ввод показаний'),
                                      DataRequired(message='Поле не должно быть пустым')],
                          render_kw={"placeholder": "Введите показания счетчика электроэнергии"})

    gas = StringField(label='Газ',
                      validators=[Length(min=1, max=7, message=f'Неверный ввод показаний'),
                                  DataRequired(message='Поле не должно быть пустым')],
                      render_kw={"placeholder": "Введите показания счетчика газа"})

    water = StringField(label='Вода',
                        validators=[Length(min=1, max=7, message=f'Неверный ввод показаний'),
                                    DataRequired(message='Поле не должно быть пустым')],
                        render_kw={"placeholder": "Введите показания счетчика воды"})

    submit = SubmitField('Отправить')

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def validate_electro(self, _):

        temp = db.session.execute(db.select(Utilities.value_electro, Utilities.date).order_by(Utilities.date.desc()).
                                  filter_by(user_id=self.user).limit(1)).one()

        if not self.electro.data.isdigit():
            raise ValidationError("Вы не ввели число")
        if temp[1].strftime('%m') == datetime.utcnow().strftime('%m'):
            raise ValidationError("Вы уже передавали показания в этом месяце")
        if int(temp[0]) > int(self.electro.data):
            raise ValidationError("Показания не могут быть меньше предыдущих")

    def validate_gas(self, _):

        temp = db.session.execute(db.select(Utilities.value_gas, Utilities.date).order_by(Utilities.date.desc()).
                                  filter_by(user_id=self.user).limit(1)).one()

        if not self.gas.data.isdigit():
            raise ValidationError("Вы не ввели число")
        if temp[1].strftime('%m') == datetime.utcnow().strftime('%m'):
            raise ValidationError("Вы уже передавали показания в этом месяце")
        if int(temp[0]) > int(self.gas.data):
            raise ValidationError("Показания не могут быть меньше предыдущих")

    def validate_water(self, _):

        temp = db.session.execute(db.select(Utilities.value_water, Utilities.date).order_by(Utilities.date.desc()).
                                  filter_by(user_id=self.user).limit(1)).one()

        if not self.water.data.isdigit():
            raise ValidationError("Вы не ввели число")
        if temp[1].strftime('%m') == datetime.utcnow().strftime('%m'):
            raise ValidationError("Вы уже передавали показания в этом месяце")
        if int(temp[0]) > int(self.water.data):
            raise ValidationError("Показания не могут быть меньше предыдущих")


class SendPayment(FlaskForm):

    payment = StringField(label="Сумма к оплате",
                          validators=[DataRequired(message='Поле не должно быть пустым'),
                                      Regexp(r'^[1-9]{1}\d*\.\d\d$',
                                             message='Введите сумму с копейками, например "1.00"')],
                          render_kw={"class": "form-control text-center"})

    submit = SubmitField('Оплатить')

    def __init__(self, *args, balance=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.payment.render_kw['value'] = abs(Decimal(balance / 100).quantize(Decimal('1.00')))


class FeedbackForm(FlaskForm):

    name = StringField(label='Имя',
                       validators=[DataRequired(message='Поле "Имя" не должно быть пустым')],
                       render_kw={"placeholder": "Введите имя"})

    tel = StringField(label='Телефон',
                      validators=[Regexp(r'^\+7-\d{3}-\d{3}-\d{4}',
                                         message='Введите номер телефона в формате "+7-XXX-XXX-XXXX"')],
                      render_kw={"placeholder": "Введите номер телефона"})

    submit = SubmitField('Оставить заявку')

    def validate_tel(self, _):
        temp = db.session.execute(db.select(Feedbacks.tel))
        for i in temp:
            if i.tel == self.tel.data:
                raise ValidationError("Вы уже отправляли заявку")
