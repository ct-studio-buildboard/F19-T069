from enum import Enum

_USERS = {
    "+18018396027" : ["Amanda", ["power tools", "heavy lifting"]]
}

_JOBS = {
    "MANUAL" : {
        "construction" : {"heavy lifting", "power tools"},
        "agriculture" : {"harvesting"}
    },
    "TECHNICAL" : {},
    "PROFESSIONAL" : {},
}

_TAGS = {

}

def getUser(num):
    #num is user phone number key
    userInfo = _USERS.get(num)
    userSkills = userInfo[1]
    return userSkills

# def matchUser(num):
#     job = matchJob(num)
#     _USERS[num][2] = job