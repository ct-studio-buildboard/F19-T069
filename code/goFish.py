import xlrd

def jobPosting():
	wb = xlrd.open_workbook('./team69.xlsx')  # Work Book
	test = wb.sheet_by_name('Job Postings Dict')  # Work Sheet
	positions = []
	skills = []
	for i in range(test.nrows):
		positions.append((test.cell(i,0)).value)
		skills.append((test.cell(i,1)).value.lower())
	jobs = {} #jobs dictionary
	for j in range(len(skills)):
		#make dictionary add job position as key look at skills column and add that as value
		skill = str(skills[j])
		# print(skill)
		skill = skill.split(', ')
		jobs[positions[j]] = skill
	return jobs