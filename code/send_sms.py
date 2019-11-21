# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACb9096772cb36e9c0ffdee7e43362cba2'
auth_token = '17c96da381557c9e5fc2cfef6e8b2df2'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Team 69 test text.",
                     from_='+12023188255',
                     to='+18018396027'
                 )

print(message.sid)
