from enum import Enum

_USERS = {

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