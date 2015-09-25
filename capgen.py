from twilio.util import TwilioCapability
from os import sys
 
account_sid = "AC7559b06de2b7bc53cc8616f248de4b73"
auth_token = sys.argv[1]
 
 
application_sid = "AP2289010d6207bca915e93a1c5582419e"
 
capability = TwilioCapability(account_sid, auth_token)
capability.allow_client_outgoing(application_sid)
token = capability.generate()
print token