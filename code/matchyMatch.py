#matchymath
import goFish
import database

def matchyMatch(num):
    matchedJobs = []
    #availJobs are a dict with job position as key and value is a list of skills
    availJobs = goFish.jobPosting()
    #userSkills is a list of a user's skills from the database
    userSkills = database.getUser(num)
    print(userSkills)
    #for key in look at the list of skills and then look at the user's skills
    #do the collections thing for comparing
    #if there is a match, add that skill to list for matched jobs
    for key in availJobs:
        desiredSkills = availJobs.get(key)
        #print("type key", type(key))
        match = set(desiredSkills).intersection(set(userSkills))
        print("desiredSkills",desiredSkills)
        print(match)
        if (len(match) > 0):
            matchedJobs.append(key)
    return matchedJobs

# from_number = "+18018396027"
# matched_jobs = matchyMatch(from_number)
# for i in range(len(matched_jobs)):
#     database._USERS[from_number][2].append(matched_jobs[i])
# print(database._USERS[from_number][2])