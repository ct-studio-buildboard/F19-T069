# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import users
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter

    message_body = request.form['Body']
    from_number = request.values.get('From')
    
    if from_number in users._USERS:
        name = users._USERS[from_number]
    else:
        name = "Friend"

    if (message_body == "RESET"):
        counter = 0
        session['counter'] = counter
    else:
        populateInfo(counter, name, message_body)

    message = '{} has messaged {} times, last text said "{}"' \
        .format(name, counter, message_body)

    resp = MessagingResponse()
    resp.message(message)
    return str(resp)

def populateInfo(counter, name, message):
    if (name in users._USERS):
        users._INFO[name][counter] = message

if __name__ == "__main__":
    app.run(debug=True)
