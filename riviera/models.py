from flask_login import UserMixin
from datetime import datetime

from riviera import db


class Users(db.Model, UserMixin):   # таблица пользователей

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    profile = db.relationship('Profiles', backref='users', uselist=False)
    utility = db.relationship('Utilities', backref='users', uselist=False)
    payment = db.relationship('Payments', backref='users', uselist=False)

    def __repr__(self):
        return f'<users {self.id}>'


class Profiles(db.Model, UserMixin):  # таблица с данными о пользователе

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tel = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Integer, default=0, nullable=False)
    account = db.Column(db.String(10), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<profiles {self.user_id}>'


class Utilities(db.Model, UserMixin):  # таблица показаний счетчиков

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    value_electro = db.Column(db.Integer, nullable=False)
    value_gas = db.Column(db.Integer, nullable=False)
    value_water = db.Column(db.Integer, nullable=False)
    summ = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<utility {self.user_id} {self.id}>'


class Service(db.Model, UserMixin):  # таблица тарифов (данные вносятся "ручками" в БД)

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(50))
    tariff = db.Column(db.Integer)

    def __repr__(self):
        return f'<service {self.id} {self.service}>'


class Payments(db.Model, UserMixin):  # таблица с платежами пользователя

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    payment_id = db.Column(db.String(100), nullable=False)
    payment_summ = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<payment, user_id: {self.user_id}, id: {self.id}, payment_id: {self.payment_id},' \
               f'payment_summ: {self.payment_summ}, status: {self.status} >'


class Houses(db.Model, UserMixin):  # таблица с домами

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(20), nullable=False)
    stead = db.Column(db.Integer)
    square = db.Column(db.Float)
    price = db.Column(db.Integer)
    description = db.Column(db.Text)


class Texts(db.Model, UserMixin):  # таблица с текстами для сайта

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50))
    label_content = db.Column(db.String(50))
    content = db.Column(db.Text)


class News(db.Model, UserMixin):  # таблица с новостями

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)


class Feedbacks(db.Model, UserMixin):  # таблица с формой на консультацию

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(100), nullable=False)
    tel = db.Column(db.String(100), nullable=False)