import os
import twilio.twiml
from twilio import twiml
from twilio.util import RequestValidator
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from flask import Flask, request
from flask import render_template
from flask import g
from flask import redirect
from config import *
import hmac
import hashlib
import time
import sqlite3
import json
import requests


app = Flask(__name__)
global url_base
url_base = "https://lendup-challenge-phonebuzz-rachitag22.c9users.io"

def setup_database():
    global DATABASE
    global conn
    global cursor
    DATABASE = "database.db"
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    table_exists = cursor.execute("SELECT name FROM sqlite_master WHERE name ='calls' and type='table'").fetchone()
    
    if not table_exists:
        conn.execute('CREATE TABLE calls (id INTEGER PRIMARY KEY, datetime DATETIME, delay INT, phonenum INT, num INT)')
    cursor.close()
    
    
def request_check():
    print("todo")

setup_database()

@app.route("/", methods=['GET', 'POST'])
def main():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM calls')
    return render_template('index.html', calls=cursor.fetchall())

@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    request_check()
    resp = twilio.twiml.Response()
    
    with resp.gather(finishOnKey="#", action="/handle-number", method="POST") as g:
        message = "Welcome to PhoneBuzz! Please enter any number, followed by the pound sign, to play!"
        g.say(message, voice="woman")

    return str(resp)

@app.route("/outbound", methods=['GET', 'POST'])
def outbound():
    data = request.data
    
    numEqualsIndex = data.index("=")
    ampIndex = data.index("&")
    phoneNum = data[numEqualsIndex+1:ampIndex]
    phoneNum = int(phoneNum)
    
    data = data[ampIndex+1:]
    delayEqualsIndex = data.index("=")
    delay = data[delayEqualsIndex+1:]
    delay = int(delay)
    
    cursor = conn.cursor()
    insert = "INSERT INTO calls (id, datetime, delay, phonenum) VALUES "
    insert = insert + "(NULL, CURRENT_TIMESTAMP," + str(delay) + "," + str(phoneNum) + ")"
    cursor.execute(insert)
    conn.commit()
    cursor.close()
     
    cursor = conn.cursor()
    global id
    id = cursor.execute("SELECT MAX(id) FROM calls")
    id = id.fetchone()
    id = id[0]
    
    global outboundUpdate
    outboundUpdate = True
    
    fromNum = TWILIO_CALLER_ID
    account_sid = TWILIO_ACCOUNT_SID
    auth_token  = TWILIO_AUTH_TOKEN
    client = TwilioRestClient(account_sid, auth_token)
    url = url_base + "/welcome"
    
    time.sleep(delay)
    call = client.calls.create(url=url, to=phoneNum, from_=fromNum)
    return ("Call outbound!")
    
@app.route("/handle-number", methods=['GET', 'POST'])
def handle_number():
        
    number_string = request.values.get('Digits', None)
    number = int(number_string)
    
    try:
        outboundUpdate
        cursor = conn.cursor()
        stmt = "UPDATE calls SET num=" + str(number) + " WHERE id=" + str(id)
        print(stmt)
        cursor.execute(stmt)
        conn.commit()
    except NameError:
        print("No update needed")
    
    resp = twilio.twiml.Response()
    message = "..."
    
    for num in xrange(1,number):
        message += ""
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

@app.route("/preset/<id>", methods=['GET', 'POST'])
def preset(id):
    cursor = conn.cursor()
    
    phoneNumStmt = "SELECT phonenum FROM calls WHERE id=" + str(id)
    phoneNum = cursor.execute(phoneNumStmt)
    phoneNum = phoneNum.fetchall()[0][0]
    
    delayStmt = "SELECT delay FROM calls WHERE id=" + str(id)
    delay = cursor.execute(delayStmt)
    delay = delay.fetchall()[0][0]
    
    numStmt = "SELECT num FROM calls WHERE id=" + str(id)
    num = cursor.execute(numStmt)
    num = num.fetchall()[0][0]

    cursor = conn.cursor()
    insert = "INSERT INTO calls (id, datetime, delay, phonenum, num) VALUES "
    insert = insert + "(NULL, CURRENT_TIMESTAMP," + str(delay) + "," + str(phoneNum) + "," + str(num) + ")"
    cursor.execute(insert)
    conn.commit()
    
    fromNum = TWILIO_CALLER_ID
    account_sid = TWILIO_ACCOUNT_SID
    auth_token  = TWILIO_AUTH_TOKEN
    client = TwilioRestClient(account_sid, auth_token)
    url = url_base + "/preset-number?num=" + str(num)
    
    time.sleep(delay)
    call = client.calls.create(url=url, to=phoneNum, from_=fromNum)
    
    return redirect("/")

@app.route("/preset-number", methods=['GET', 'POST'])
def preset_number():
    number = request.args.get("num")
    number = int(number)
    
    resp = twilio.twiml.Response()
    message = "Welcome to PhoneBuzz Replay! The number is " + str(number) + "..."
    resp.say(message, voice="woman")
    
    message = ""
    
    for num in xrange(1,number):
        message += ""
        
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
    
    return redirect("/")
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), use_reloader=False)