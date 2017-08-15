import os
from datetime import timedelta

DEBUG = True

SESSION_TYPE = 'redis'
SERVER_NAME = 'httpbin.local'

SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/r'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True
SECRET_KEY = os.urandom(10)
PERMANENT_SESSION_LIFETIME = timedelta(seconds=30)


#debug setting
DEBUG_TB_INTERCEPT_REDIRECTS = False