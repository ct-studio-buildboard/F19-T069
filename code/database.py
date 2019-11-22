_USERS = {
    "+18018396027" : ["Amanda", ['heavy lifting', 'r', 'python'], []]
}

_JOBS = {
    "Manual" : {
        "construction" : {"heavy lifting", "power tools"},
        "agriculture" : {"harvesting", "crop growing", "livestock farming", "poultry farming", "shepherding"}
    },
    "Technical" : {
        "coding" : {"Python", "MATLAB", "C++", "C", "javascript", "PHP", "HTML", "SQL", "R", "C#"},
        "MS Office" : {"Excel", "Word", "PowerPoint", "Outlook"}
    },
    "Professional" : {
        "medical" : {"therapy", "physical therapy", "dentistry", "gynecology", "pharmacy"},
        "education" : {"teaching", "tutoring", "school application advising", "curriculum designing"}
    }
}

def getUser(num):
    #num is user phone number key
    userInfo = _USERS.get(num)
    userSkills = userInfo[1]
    return userSkills