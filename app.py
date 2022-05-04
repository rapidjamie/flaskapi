import flask
from flask import request, jsonify
import re
import json
import requests


app = flask.Flask(__name__)

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@app.route('/', methods=['GET'])
def home():
    return jsonify({'msg': 'Server running'})


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/validateEmail/<email>')
def email(email):
    return isValid(email)


def isValid(emailInput):

    if re.fullmatch(regex, emailInput):
        response = {
            "email" : emailInput,
            "domain" : emailInput.split("@")[1], 
            "isValid": "Valid email"
        }
        return json.dumps(response)
    else:
        response = {
            "email" : emailInput,
            "isValid": "invalid email"
        }
        return  json.dumps(response)


@app.route('/getAllNames')
def index():
    dummy_data = [{
        'id': 1,
        'name': 'Jeff Ding',
        'email': 'jeff@rapidapi.com'
    }, {
        'id': 2,
        'name': 'Yih Jeff Test',
        'email': 'jeff@rapidapi.com'
    }]

    return jsonify(dummy_data)





def sendEmail(emailAddress):

    payload = {
	    "personalizations": [
		    {
			    "to": [{"email": emailAddress}],
			    "subject": "Hello, World!"
		    }
	],
	"from": {"email": "jeff@rapidapi.com"},
	"content": [
		    {
			    "type": "text/plain",
			    "value": "Hello, World!"
		    }
	    ]
    }  
    url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"

    headers = {
	    "content-type": "application/json",
	    "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com",
	    "X-RapidAPI-Key": "956abe1d10mshd6ea462a6a7e4ebp1e4099jsn70d018b4c2ea"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)
