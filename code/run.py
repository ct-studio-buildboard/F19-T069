# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import database, job_input
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

category = ""
industries = []
list_jobs = []
tmp_skills = []

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    global list_jobs, tmp_skills, industries, category
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter

    message_body = request.form['Body']
    from_number = request.values.get('From')
    
    if (message_body == "RESET"):
        counter = 0
        session['counter'] = counter

    if (session['counter'] == 0):
        message = "\nLooks like you're a new user! What is your name?"
    elif (session['counter'] == 1):
        database._USERS[from_number] = [message_body.strip(), []]
        message = ("\nThanks {}! Let's create your profile. Which category would you like to fill out first?\n1: MANUAL\n2: TECHNICAL\n3: PROFESSIONAL").format(database._USERS[from_number][0])
    elif (session['counter'] == 2):
        if (int(message_body.strip()) == 1): # MANUAL
            category = "MANUAL"
        elif (int(message_body.strip()) == 2): # TECHNICAL
            category = "TECHNICAL"
        elif (int(message_body.strip()) == 3): # PROFESSIONAL
            category = "TECHNICAL"
        list_jobs = database._JOBS[category] # get JOBS in CATEGORY
        msg = "\nChoose an industry to select your skills (you'll be able to come back to these later!):\n"
        c = 1
        # print(list_jobs)
        for ind in list_jobs:
            msg += str(c) + ": " + ind + "\n"
            print(ind)
            industries.append(ind)
            c += 1
        message = msg
        print("industries", industries)
    elif (session['counter'] == 3):
        job = industries[int(message_body.strip()) - 1] # construction
        msg = "\n List your skills in this industry:\n"
        c = 1
        tmp_skills = []
        for s in database._JOBS[category][job]:
            msg += str(c) + ": " + s + "\n"
            tmp_skills.append(s)
            c += 1
        message = msg
    elif (session['counter'] == 4): # skills selected
        user_skill = message_body.replace(" ", "").split(",")
        for i in range(len(user_skill)):
            user_skill[i] = int(user_skill[i])
        print("hello?")
        print(len(user_skill), user_skill, tmp_skills)
        for i in range(len(user_skill)):
            print(i)
            database._USERS[from_number][1].append(tmp_skills[i])
        message = ("{}, you've said your skills are: {}").format(database._USERS[from_number][0], database._USERS[from_number][1])
        print("tmp skills ", type(tmp_skills[i-1]), tmp_skills[i-1])
        print(database._USERS[from_number][1])
        message = message + "\nEnter:\n1: To go back to industries\n2: To save and exit profile building"
    elif (session['counter'] == 5): # save and EXIT
        if (int(message_body.strip()) == 2): 
            message = "\nYou've completed your profile!\nHere's the jobs that match your profile:\n"

    resp = MessagingResponse()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)