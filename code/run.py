# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import database, matchyMatch
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

_IDX = 0

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    global list_jobs, tmp_skills, industries, category, _FLOW, _IDX
    _IDX = session.get('_IDX', 0)
    session['_IDX'] = _IDX

    message_body = request.form['Body']
    from_number = request.values.get('From')
    
    if (message_body.strip().lower() == "reset"):
        _IDX = 0
        session['_IDX'] = 0

    if (session['_IDX'] == 0):
        message = "\nLooks like you're a new user! What is your name?"
        _IDX = 1
    elif (session['_IDX'] == 1):
        if (from_number not in database._USERS):
            database._USERS[from_number] = [message_body.strip(), [], []]
        message = ("\nThanks {}! Let's create your profile. Which category would you like to fill out first?\n1: MANUAL\n2: TECHNICAL\n3: PROFESSIONAL").format(database._USERS[from_number][0])
        _IDX = 2
    elif (session['_IDX'] == 2):
        msg = "\nChoose an industry to select your skills (you'll be able to come back to these later!):\n"
        if (int(message_body.strip()) == 1): # MANUAL
            category = "MANUAL"
            _IDX = 3
        elif (int(message_body.strip()) == 2): # TECHNICAL
            category = "TECHNICAL"
            _IDX = 3
        elif (int(message_body.strip()) == 3): # PROFESSIONAL
            category = "PROFESSIONAL"
            _IDX = 3
        else:
            message = "Sorry, try again."
        if (int(message_body.strip()) <= 3):
            industries = []
            list_jobs = database._JOBS[category] # get JOBS in CATEGORY
            c = 1
            for ind in list_jobs:
                msg += str(c) + ": " + ind + "\n"
                industries.append(ind)
                c += 1
            message = msg
    elif (session['_IDX'] == 3):
        job = industries[int(message_body.strip()) - 1] # construction
        msg = "\n List your skills in this industry:\n"
        c = 1
        tmp_skills = []
        for s in database._JOBS[category][job]:
            msg += str(c) + ": " + s + "\n"
            tmp_skills.append(s)
            c += 1
        message = msg
        _IDX = 4
    elif (session['_IDX'] == 4): # skills selected
        user_skill = message_body.replace(" ", "").split(",")
        for i in range(len(user_skill)):
            user_skill[i] = int(user_skill[i]) - 1
        for i in range(len(user_skill)):
            database._USERS[from_number][1].append(tmp_skills[user_skill[i]])
        str_skills = ""
        for i in range(len(database._USERS[from_number][1])):
            str_skills += database._USERS[from_number][1][i] + ", "
        message = ("{}, you've said your skills are: {}").format(database._USERS[from_number][0], str_skills[:len(str_skills) - 2])
        message = message + "\nEnter:\n1: To go back to industries\n2: To save and view jobs."
        _IDX = 5
    elif (session['_IDX'] == 5): 
        if (int(message_body.strip()) == 1): 
            _IDX = 1
            message = "\nBringing you back to the industries list... Reply to proceed.\n"
        elif (int(message_body.strip()) == 2): 
            _IDX = 6
            matched_jobs = matchyMatch.matchyMatch(from_number)
            for i in range(len(matched_jobs)):
                database._USERS[from_number][2].append(matched_jobs[i])
            message = "\nYou've completed your profile!\nFinding the jobs that match...\nReply to view jobs."
    elif (session['_IDX'] == 6): # PRINT JOBS
        message = "\nHere they are:\n"
        for i in range(len(database._USERS[from_number][2])):
            message += database._USERS[from_number][2][i] + ", "
            message = message[:len(message) - 2]
    else:
        message = "Under construction :)"

    session['_IDX'] = _IDX
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)