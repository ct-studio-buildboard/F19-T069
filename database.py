from enum import Enum

_USERS = {
    "8018396027" : ["Amanda", ["power tools", "heavy lifting"]]
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

# def getUser(num):
#     return num

# def matchUser(num):
#     job = matchJob(num)
#     _USERS[num][2] = job