# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd843f2683f2b16a5fdedce91c16e4410'
auth_token = '53ada0a1ec1c9fb87fa187b6e0fa5255'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Team 69 test text.",
                     from_='+12054967693',
                     to='+18018396027'
                 )

print(message.sid)
