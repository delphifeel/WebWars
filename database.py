from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
#from models.user import User



APP = Flask(__name__)
APP.config.from_object('config')
DB = SQLAlchemy(APP)

login_manager = LoginManager()
login_manager.init_app(APP)
login_manager.login_view = 'login'

@login_manager.user_loader
def user_loader(user_id):
    return User.query.filter_by(id=user_id).first()