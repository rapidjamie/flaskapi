import flask
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import request, jsonify
import re

from marshmallow import Schema, fields

app = flask.Flask(__name__)

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

spec = APISpec(
    title='flask-api-non-gateway',
    version='1.0.0',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)


@app.route('/', methods=['GET'])
def home():
    return 'hello world'


@app.route('/api/swagger.json', methods=['GET'])
def createSwaggerSpec():
    return jsonify(spec.to_dict())


class NameResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()


class NameListResponseSchema(Schema):
    name_list = fields.List(fields.Nested)


@app.route('/getAllNames')
def index():
    """Get List of Names in System
    ---
    get:
        description: Get List of Names in System
        responses:
            200:
                description: Return a name list
                content:
                    application/json:
                        schema: NameListResponseSchema
    """
    dummy_data = [{
        'id': 1,
        'name': 'Jeff Ding',
        'email': 'jeff@rapidapi.com'
    }, {
        'id': 1,
        'name': 'Jeff Ding',
        'email': 'jeff@rapidapi.com'
    }]

    return NameListResponseSchema().dump({'name_list': dummy_data})


@app.route('/validateEmail/<email>')
def email(email):
    return isValid(email)


def isValid(emailInput):
    if re.fullmatch(regex, emailInput):
        return "{Valid email}"
    else:
        return "{Invalid email}"
