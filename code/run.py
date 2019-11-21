# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import database, job_input
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
    
    # if from_number in database._USERS:
    #     name = database._USERS[from_number]
    # else:
        # name = message_body.strip()

    if (message_body == "RESET"):
        counter = 0
        session['counter'] = counter

    if (session['counter'] == 0):
        message = "Looks like you're a new user! What is your name?"
    elif (session['counter'] == 1):
        database._USERS[from_number] = [message_body.strip(), []]
        print(database._USERS)
        message = ("Thanks {}! Let's create your profile. What are your skills?").format(database._USERS[from_number][0])
    elif (session['counter'] == 2):
        skills = message_body.split(",")
        print(database._USERS[from_number])
        database._USERS[from_number][1].extend(skills)
        message = ("{}, you've said your skills are: {}").format(database._USERS[from_number][0], database._USERS[from_number][1])

    resp = MessagingResponse()
    resp.message(message)
    return str(resp)

# def populateInfo(counter, name, message):
#     if ( name in users._USERS):
#         users._INFO[name][counter] = message

if __name__ == "__main__":
    job_input.createJob()
    print("Job created!")
    app.run(debug=True)