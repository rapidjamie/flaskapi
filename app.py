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
    dummy_data = [{
        'id': 1,
        'name': 'Jeff Ding',
        'email': 'jeff@rapidapi.com'
    }, {
        'id': 2,
        'name': 'Jeff Ding2',
        'email': 'jeff@rapidapi.com'
    }]

    return jsonify(dummy_data)


@app.route('/validateEmail/<email>')
def email(email):
    return isValid(email)


@app.route('/test')
def test():
    return "demo"


def isValid(emailInput):
    if re.fullmatch(regex, emailInput):
        return jsonify("{'isValid' : 'Valid email'}")
    else:
        return  jsonify("{'isValid' : 'Invalid email'}")
