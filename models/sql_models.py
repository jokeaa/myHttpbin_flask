# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_security import UserMixin as ss
db = SQLAlchemy()


class Permission(object):
    LOGIN = 0x01
    EDITOR = 0x02
    OPERATOR = 0x04
    ADMINISTRATOR = 0xff

    PERMISSION_MAP = {
        LOGIN:('login','Login user'),
        EDITOR:('editor','Editor'),
        OPERATOR:('op','Operator'),
        ADMINISTRATOR:('admin','Super administrator')
    }



class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, index=True)


class User(db.Model,UserMixin):
    __tablename__ = 'user'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True, server_default=db.FetchedValue())
    email = db.Column(db.String(25))
    password = db.Column(db.String(25))
    perissions = db.Column(db.Integer,default=Permission.LOGIN)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return "1"