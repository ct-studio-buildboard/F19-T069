# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import database, matchyMatch
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from googletrans import Translator

# The session object makes use of a secret key.
SECRET_KEY = 'Team69'
app = Flask(__name__)
app.config.from_object(__name__)

# Kinda yikes global vars
category = ""
industries = []
list_jobs = []
tmp_skills = []

translator = Translator()

# Pointer in the state machine
_PREV_IDX = 0
_IDX = 0
_prev_msg = ""

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    global list_jobs, tmp_skills, industries, category, translator, _IDX, _PREV_IDX, _prev_msg

    # Initialize this _IDX for this user if it doesn't exist
    _IDX = session.get('_IDX', 0)
    session['_IDX'] = _IDX

    # Grab received parameters
    message_body = request.form['Body']
    from_number = request.values.get('From')
    
    # Reset EVERYTHING
    if (message_body.strip().lower() == "reset"):
        _IDX = 0
        session['_IDX'] = 0
        database._USERS = {} # INCLUDING USERS

    # Allow to change language at any point in process
    if (message_body.strip().lower() == "change language"):
        _PREV_IDX = _IDX
        _IDX = -2
        message = "\nWant to change the language? Enter the language code:\n(e.g. af for Afrikaans, el for Greek, en for English, vi for Vietnamese...)"

    elif (session['_IDX'] == -2):  # Change language
        code = message_body.strip().lower()
        if (code not in database._LANGUAGES):
            message = "\nSorry, that's not a valid language code. Try again."
        else:
            database._USERS[from_number][3] = code
            message = "\nYou've switched your language to: " + database._LANGUAGES[code].capitalize() + ".\n" + _prev_msg
            _IDX =_PREV_IDX
        
    elif (session['_IDX'] == 0):  # Restarting!
        message = "\nLooks like you're a new user! What is your name?"
        _IDX = 1 # Go to CATEGORIES

    elif (session['_IDX'] == 1): # Choosing categories
        if (from_number not in database._USERS):
            database._USERS[from_number] = [message_body.strip(), [], [], 'en']
        message = ("\nThanks {}! Let's create your profile. Which category would you like to fill out first?\n1: Manual\n2: Technical\n3: Professional").format(database._USERS[from_number][0])
        _IDX = 2 # Go to INDUSTRY

    elif (session['_IDX'] == 2): # choosing industry
        msg = "\nChoose an industry to select your skills (you'll be able to come back to these later!):\n"
        if (int(message_body.strip()) <= 3):
            if (int(message_body.strip()) == 1): # MANUAL
                category = "Manual"
            elif (int(message_body.strip()) == 2): # TECHNICAL
                category = "Technical"
            elif (int(message_body.strip()) == 3): # PROFESSIONAL
                category = "Professional"
            industries = []
            list_jobs = database._JOBS[category] # get JOBS in CATEGORY
            c = 1
            # Iterate through JOBS in CATEGORY
            for ind in list_jobs:
                msg += str(c) + ": " + ind + "\n"
                industries.append(ind) # add to this global list
                c += 1
            message = msg
            _IDX = 3
        else: # didn't choose 1-3
            message = "Sorry, try again.\n" + _prev_msg

    elif (session['_IDX'] == 3): # List SKILLS from JOB
        job = industries[int(message_body.strip()) - 1] # grab the JOB chosen (from INDUSTRY)
        if (job not in database._JOBS[category]):
            message = "Sorry, try again.\n" + _prev_msg
        else:
            msg = "\n List your skills in this industry:\n"
            c = 1
            tmp_skills = []

            # Iterate through SKILLS in CHOSEN JOB
            for s in database._JOBS[category][job]:
                msg += str(c) + ": " + s + "\n"
                tmp_skills.append(s.lower()) # add to global tmp_skills 
                c += 1
            message = msg
            _IDX = 4 # go to SKILL SELECTION

    elif (session['_IDX'] == 4): # Select SKILLS from LIST
        user_skill = message_body.replace(" ", "").split(",") # numbers entered

        # Turn them all into ints
        for i in range(len(user_skill)): 
            user_skill[i] = int(user_skill[i]) - 1 # turn into ints

        # Append skills based on entered values
        for i in range(len(user_skill)):
            database._USERS[from_number][1].append(tmp_skills[user_skill[i]]) 

        str_skills = "" # Accumulator to print out
        # Build up the list of skills without []s
        for i in range(len(database._USERS[from_number][1])):
            str_skills += database._USERS[from_number][1][i] + ", "
        message = ("{}, you've said your skills are: {}").format(database._USERS[from_number][0], str_skills[:len(str_skills) - 2])
        message = message + "\nEnter:\n1: To go back to industries\n2: To save and view jobs."
        _IDX = 5 # Go to next step

    elif (session['_IDX'] == 5): # Branching step
        if (int(message_body.strip()) == 1): # Go back to industry
            _IDX = 1
            message = "\nBringing you back to the industries list... Reply to proceed.\n"
        elif (int(message_body.strip()) == 2): # Look at jobs
            _IDX = 6
            matched_jobs = matchyMatch.matchyMatch(from_number) # grab job matches
            for i in range(len(matched_jobs)):
                database._USERS[from_number][2].append(matched_jobs[i])
            message = "\nYou've completed your profile!\nFinding the jobs that match...\nReply to view jobs."

    elif (session['_IDX'] == 6): # PRINT JOBS
        message = "\nHere they are:\n"
        # Print out jobs matched
        for i in range(len(database._USERS[from_number][2])):
            message += database._USERS[from_number][2][i] + ", "
        message = message[:len(message) - 2]
    else:
        message = "Under construction :)"

    session['_IDX'] = _IDX
    resp = MessagingResponse()
    if (_IDX >= 0): # If not changing language, save where you were
        _prev_msg = message

    # Translate message if language choice not English
    if (from_number in database._USERS):
        if (database._USERS[from_number][3] != 'en'):
            message = translator.translate(message, dest=database._USERS[from_number][3]).text
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)