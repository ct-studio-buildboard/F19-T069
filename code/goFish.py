import xlrd

wb = xlrd.open_workbook('team69.xlsx')  # Work Book
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
        category = test.cell(i,1).value
        industry = test.cell(i,2).value
        skills = test.cell(i,3).value
        skills = skills.split(', ')
        skills = set(skills)

        if (category not in categories):
            industries[industry] = skills
            categories[category] = {industry : industries[industry]}
        else:
            if (industry not in industries):
                categories[category][industry] = skills
    return categories