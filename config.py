'''
Configuration Settings
'''

TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxx" 
TWILIO_AUTH_TOKEN = "yyyyyyyyyyyyyyyy"
TWILIO_CALLER_ID = "+17778889999"

import os
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_CALLER_ID = os.environ.get('TWILIO_CALLER_ID', None)
TWILIO_APP_SID = os.environ.get('TWILIO_APP_SID', None)