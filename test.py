from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_security import LoginForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_mail import Mail

app = Flask(__name__)
app.config.from_pyfile('setting.py')

db = SQLAlchemy(app)
# mail = Mail()

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                       )


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.String(255))

class ExtendLoginForm(LoginForm):
    test = StringField('test',[DataRequired])


user_datastore = SQLAlchemyUserDatastore(db,User,Role)
security = Security(app,user_datastore,login_form=ExtendLoginForm)

@security.context_processor
def security_context_processor():
    return dict(hello='world')

@app.before_first_request
def create_user():
    db.drop_all()
    db.create_all()
    user_datastore.create_user(email='422740565@qq.com',password='password')
    db.session.commit()

@app.route('/')
@login_required
def home():
    return 'hello'



if __name__ == "__main__":
    app.run()