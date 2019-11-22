import xlrd

wb = xlrd.open_workbook('C:/Users/ChristineKu/Documents/GitHub/F19-T069/code/team69.xlsx')  # Work Book
test = wb.sheet_by_name('Job Postings Dict')  # Work Sheet

def jobPosting():
    global wb, test
    positions = []
    skills = []
    for i in range(test.nrows):
        positions.append((test.cell(i,0)).value)
        skills.append((test.cell(i,3)).value.lower())
        jobs = {} #jobs dictionary
    for j in range(len(skills)): #make dictionary add job position as key look at skills column and add that as value
        skill = str(skills[j])
        skill = skill.split(', ')
        jobs[positions[j]] = skill
    return jobs

def database():
    global wb, test
    categories = {}
    industries = {}
    for i in range(test.nrows):
        skills = test.cell(i,3).value
        skills = skills.split(', ')
        skills = set(skills)
        if ( not test.cell(i,1).value in categories.keys()):
            industries[test.cell(i,2).value] = skills
            categories[test.cell(i,1).value] = industries

        if (not test.cell(i,2).value in industries):
            industries[test.cell(i,2).value] = skills
        
        for skill in skills:
            if (skill in industries.get(test.cell(i,2).value)):
                industries[test.cell(i,2).value].add(skill)
    jobs = {}
    jobs['_JOBS'] = categories
    return jobs