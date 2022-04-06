import flask
from flask import request, jsonify
import re

app = flask.Flask(__name__)

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@app.route('/', methods=['GET'])
def home():
    return 'hello world'


@app.route('/getAllNames')
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})


@app.route('/validateEmail/<email>')
def email(email):
    return isValid(email)


def isValid(email):
    if re.fullmatch(regex, email):
        return "Valid email"
    else:
        return "Invalid email"
