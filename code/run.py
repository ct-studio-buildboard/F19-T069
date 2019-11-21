# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "+18018396027": "Amanda",
    "+12349013030": "Finn",
    "+12348134522": "Chewy",
}

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter

    number = request.form['From']
    message_body = request.form['Body']
    from_number = request.values.get('From')
    
    if (message_body == "RESET"):
        counter = 0
        session['counter'] = counter
    
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Friend"

    message = '{} has messaged {} times, last text said "{}"' \
        .format(name, counter, message_body)

    resp = MessagingResponse()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
