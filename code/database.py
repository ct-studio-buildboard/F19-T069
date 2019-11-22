import goFish
_USERS = {
    "+18018396027" : ["Amanda", ['heavy lifting', 'r', 'python'], []]
}

_JOBS = goFish.database()

print(_JOBS)

def getUser(num):
    #num is user phone number key
    userInfo = _USERS.get(num)
    userSkills = userInfo[1]
    return userSkills