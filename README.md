# Rachit's PhoneBuzz

We all know the classic game Fizz Buzz. PhoneBuzz (created as a LendUp code challenge) lets you play Fizz Buzz through your phone, using Twilio. You can either call the PhoneBuzz hotline and enter a number to listen to the Fizz Buzz leading up to that number, or have PhoneBuzz call you. You can also see a history of the calls PhoneBuzz has made to you, and replay any of them!

## Built With

PhoneBuzz was built with Flask, HTML/CSS/JS, and Twilio.

## Try It Out

You can try out the app at (https://rach-phonebuzz.herokuapp.com/). NOTE: You will only be able to use Option 1 (Call the PhoneBuzz hotline). Option 2 won't work because my Twilio account doesn't have your phone number as a verified number.

## Getting Started

First, clone the repo.

### Prerequisites

Of course, you need to have Python and pip installed. Make sure you also install the dependencies specified in requirements.txt (Twilio, requests, etc.).

```
pip install _______
```

### Setting Up

Next, add your Twilio credentials as environment variables, and config.py will automatically import them. Alternatively, you can hard-code them into config.py (discouraged if you're uploading for the public to see).

```
export TWILIO_ACCOUNT_SID = __________________
export TWILIO_AUTH_TOKEN = ___________________
export TWILIO_CALLER_ID = ____________________
export TWILIO_APP_SID = ______________________
```

You must also change the URL's in app.py and scripts.js to the URL of wherever you'll be hosting your app.

In app.py, change this line:

```
url_base = "https://rach-phonebuzz.herokuapp.com"
```

In scripts.js, change this line:

```
var base_url = "https://rach-phonebuzz.herokuapp.com";
```

Also, after you make a new Twilio app, make sure the voice URL points to the URL for your clone!

## Thank You!
Hopefully, everything goes well. Feel free to email me at (rachitagarwal0202@gmail.com).