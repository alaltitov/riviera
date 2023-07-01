# -----------------------------------------------------------
# Пример реализации сайта коттеджного поселка с регистрацией,
# авторизацией, личным кабинетом пользователя, оплатой
# коммунальных платежей через Ю-Кассу с простой аналитикой.
#
# (C) 2023 Алексей Титов, Одинцово, Россия
# email alaltitov@yandex.ru
# -----------------------------------------------------------

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import uuid

application = Flask(__name__)
application.config['SECRET_KEY'] = uuid.uuid4().hex
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/owners_mysql'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)

from riviera import models, routes
from riviera.models import Users

login_manager = LoginManager(application)
login_manager.login_view = 'login_page'
login_manager.login_message = 'Авторизуйтесь для доступа к личному кабинету'
login_manager.login_message_category = 'success'


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Users).get(user_id)
