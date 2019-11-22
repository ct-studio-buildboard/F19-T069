from enum import Enum

_USERS = {

}

_JOBS = {
    "MANUAL" : {
        "construction" : {"heavy lifting", "power tools"},
        "agriculture" : {"harvesting", "crop growing", "livestock farming", "poultry farming", "shepherding"}
    },
    "TECHNICAL" : {
        "coding" : {"Python", "MATLAB", "C++", "C", "javascript", "PHP", "HTML", "SQL", "R", "C#"},
        "MS Office" : {"Excel", "Word", "PowerPoint", "Outlook"}
    },
    "PROFESSIONAL" : {
        "medical" : {"therapy", "physical therapy", "dentistry", "gynecology", "pharmacy"},
        "education" : {"teaching", "tutoring", "school application advising", "curriculum designing"}
    },
}

_TAGS = {

}

def getUser(num):
    #num is user phone number key
    userInfo = _USERS.get(num)
    userSkills = userInfo[1]
    return userSkills