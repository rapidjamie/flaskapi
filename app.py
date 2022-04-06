import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    arg = request.args['arg1']
    return 'hello world'


@app.route('/getName')
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})