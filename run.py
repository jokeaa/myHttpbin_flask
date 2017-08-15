# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Response, jsonify, json, redirect, url_for, Blueprint, session
from flask_login import LoginManager, login_required, login_user, logout_user, fresh_login_required, login_fresh
from flask_debugtoolbar import DebugToolbarExtension
from modules import now
from flask_session import Session
from models.sql_models import User, Post
from flask_sqlalchemy import SQLAlchemy

from flask_security.utils import login_user

from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm

app = Flask(__name__,template_folder='templates')

app.config.from_pyfile('setting.py')

toolbar = DebugToolbarExtension(app)

login_manager = LoginManager()
login_manager.session_protection = 'null'
login_manager.login_view = 'auth.login'
login_manager.refresh_view = 'relogin'
login_manager.init_app(app)
# login_manager.remember_cookie_duration = timedelta(seconds=6000)

CSRFProtect(app)
Session(app)
db = SQLAlchemy(app)

app.register_blueprint(now, subdomain="now")
auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    user = User()
    return user


# 自定义login_view操作
# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return login()

# @login_manager.needs_refresh_handler
# def refresh_need():
#     return relogin()

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/ip/')
def show_ip():
    print request.remote_addr
    print jsonify(origin=request.remote_addr)
    # return Response(json.dumps({"origin":request.remote_addr}),mimetype='application/json')
    return jsonify(origin=request.remote_addr)


@app.route('/user-agent/')
def show_UA():
    return json.dumps({"UA": request.headers.get('User-Agent')})


@app.route('/headers/')
def show_Headers():
    return jsonify(http_header=request.headers)


@app.route('/links/<int:n>/<int:offset>/')
def link_page(n, offset):
    print request.args
    n = min(max(1, n), 50)
    return render_template('link_template.html', n=n, offset=offset)


@app.route('/links/<int:n>/')
def links(n):
    # return redirect(url_for(link_page,n=n,offset=0))
    return redirect(url_for('link_page', n=n, offset=0))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    session.permanet = True
    user = User()
    login_user(user, remember=True)
    test = User(name='test1')
    db.session.add(test)
    return 'login page'


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    print login_fresh()
    logout_user()
    return 'logout page'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        print form.name.data
        print form.email.data
        print form.password.data

        return 'Register successed'
    return render_template('register.html',form=form)


@app.route('/test')
@login_required
def test():
    print login_fresh()
    # print session.items()
    return 'yes,you are allowed'


@app.route('/new')
@fresh_login_required
def secret():
    return 'you need to fresh to see it '


@app.route('/relogin')
def relogin():
    print login_fresh()
    return 'you are relogin'


app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
