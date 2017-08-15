#coding:utf-8
from flask_wtf import Form
from wtforms import StringField,PasswordField
from wtforms.validators import length,DataRequired,EqualTo
# from wtforms.ext.i18n.form import Form



class RegistrationForm(Form):

    name = StringField(u'用户名',validators=[length(min=4,max=25),DataRequired(u'请输入用户名')])
    email = StringField('Email',validators=[length(min=6,max=35),DataRequired()])
    password = PasswordField('Password',validators=[length(min=6,max=25),DataRequired(),EqualTo('confirm',message='Passwords must match')])
    confirm = PasswordField('Repeat Password')

