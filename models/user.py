from flask.ext.login import UserMixin
from database import DB


class User(DB.Model, UserMixin):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(40), nullable=False)
    password = DB.Column(DB.String(80), nullable=False)