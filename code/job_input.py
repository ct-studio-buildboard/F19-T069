import database

def createJob():
    _jobs = database._JOBS
    _tags = database._TAGS
    newJobID = len(_jobs)
    intxt = input("To create a new job, post relevant tags: ")
    print("You said:", intxt)
    intxt = intxt.split(",")
    for t in intxt:
        if (t not in _tags):
            _tags[t] = 0
        else:
            _tags[t] += 1
    _jobs[newJobID] = intxt
    print("Jobs", _jobs)
    print("Tags", _tags)