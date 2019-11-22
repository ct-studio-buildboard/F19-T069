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

# def getUser(num):
#     return num

# def matchUser(num):
#     job = matchJob(num)
#     _USERS[num][2] = job