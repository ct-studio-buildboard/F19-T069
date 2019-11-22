#matchymath
import goFish
import database

def matchyMatch(num):
    #availJobs are a dict with job position as key and value is a list of skills
    availJobs = goFish.jobPosting()
    #userSkills is a list of a user's skills from the database
    userSkills = database.getUser(num)
    #for key in look at the list of skills and then look at the user's skills
    #do the collections thing for comparing
    #if there is a match, add that skill to list for matched jobs
    for key in availJobs:
        desiredSkills = availJobs.get(key)
        match = set(desiredSkills).intersection(userSkills)
    return match
