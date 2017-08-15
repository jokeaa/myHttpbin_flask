from flask import Blueprint,g
import json,time

from flask.json import jsonify

now = Blueprint('now',__name__)

@now.route('/')
def home():
    return jsonify(nowTime=time.ctime())