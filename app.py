import os
import twilio.twiml
from twilio import twiml
from twilio.util import RequestValidator
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from flask import Flask, request
from flask import render_template
from config import *
import hmac
import hashlib
import time


app = Flask(__name__)

def request_check():
    print("todo")

@app.route("/", methods=['GET', 'POST'])
def main():
    #outbound()
    return render_template("index.html")

@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    request_check()
    resp = twilio.twiml.Response()
    
    with resp.gather(finishOnKey="#", action="/handle-number", method="POST") as g:
        message = "Welcome to PhoneBuzz! Please enter any sequence of numbers, followed by the pound sign."
        g.say(message, voice="woman")

    return str(resp)

@app.route("/outbound", methods=['GET', 'POST'])
def outbound():
    delaySeconds = 10
    toNum = "+13012813692"
    fromNum = TWILIO_CALLER_ID
    account_sid = TWILIO_ACCOUNT_SID
    auth_token  = TWILIO_AUTH_TOKEN
    client = TwilioRestClient(account_sid, auth_token)
    url = "https://lendup-challenge-phonebuzz-rachitag22.c9users.io/welcome"
    
    time.sleep(delaySeconds)
    call = client.calls.create(url=url, to=toNum, from_=fromNum)
    
@app.route("/handle-number", methods=['GET', 'POST'])
def handle_number():
    
    number_string = request.values.get('Digits', None)
    resp = twilio.twiml.Response()
    message = "..."
    
    for ch in number_string:
    	message += " "
    	num = int(ch)
    	
    	if num % 3 == 0 and num % 5 == 0:
    		message += "Fizz Buzz"
    	elif num % 3 == 0:
    		message += "Fizz"
    	elif num % 5 == 0:
    		message += "Buzz"
    	else:
    		message += str(num)
    	
    	message += "..."
    	
    message += "......Thank you for using PhoneBuzz!"
    resp.say(message, voice="woman")
    return str(resp)

@app.route("/preset-number", methods=['GET', 'POST'])
def preset_number():
    print("FJSLDKJF")


app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), use_reloader=False)