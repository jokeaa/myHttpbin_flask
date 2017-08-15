from flask_wtf import Form
from wtforms import StringField,PasswordField
from wtforms.validators import length,DataRequired,EqualTo

class RegistrationForm(Form):
    name = StringField('Username',validators=[length(min=4,max=25),DataRequired()])
    email = StringField('Email',validators=[length(min=6,max=35),DataRequired()])
    password = PasswordField('Password',validators=[length(min=6,max=25),DataRequired(),EqualTo('confirm',message='Passwords must match')])
    confirm = PasswordField('Repeat Password')

