import xlrd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def jobPosting():
    #authorization
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/ChristineKu/Documents/GitHub/F19-T069/code/ReConnect-8253b28955c7.json', scope)

    gc = gspread.authorize(credentials)
    wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Rbhfg2A8ZfQSqvWp1hjfENsCaZGHFyb9zFZw2g2RAfY/edit?usp=sharing')
    ws = wb.worksheet("Sheet1")
    list_of_lists = ws.get_all_values()
    #print(len(list_of_lists[0]))
    i=10
    jobs = {}
    for p in range(len(list_of_lists)-1):
        currentRow = 1+p
        #print(currentRow)
        #pos = ws.cell(k+p,9).value
        pos = list_of_lists[currentRow][9]
        #print(pos)
        for j in range(len(list_of_lists[0])-i):
            #print(j)
            #print(i+j)
            colTitle = list_of_lists[0][i+j]
            #print(colTitle)
            if pos in colTitle:
                skills = list_of_lists[currentRow][i+j]
                #print(skills)
                skillz = skills.split(', ')
            else:
                continue
            company = list_of_lists[currentRow][1]
            email = list_of_lists[currentRow][2]
            location = list_of_lists[currentRow][5]
            startDate = list_of_lists[currentRow][7]
            #description = ws.cell(currentRow,)
            # the position already exists, make the key pos+str(some increment)
            jobs[pos] = [company, email, location, startDate, skillz]
    return jobs

def database():
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    
    credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/ChristineKu/Documents/GitHub/F19-T069/code/ReConnect-8253b28955c7.json', scope)

    gc = gspread.authorize(credentials)
    wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Rbhfg2A8ZfQSqvWp1hjfENsCaZGHFyb9zFZw2g2RAfY/edit?usp=sharing')
    ws = wb.worksheet("Sheet1")
    list_of_lists = ws.get_all_values()
    categories = {}
    industries = {}
    for i in range(len(list_of_lists)-1):
        currentRow = i+1
        category = list_of_lists[currentRow][8]
        industry = list_of_lists[currentRow][9]
        print(len(list_of_lists[0]))
        for j in range(len(list_of_lists[0])-10):
            colTitle = list_of_lists[0][10+j]
            if industry in colTitle:
                skills = list_of_lists[currentRow][10+j]
                skillz = skills.split(', ')
            else:
                continue
        skillz = set(skillz)

        if (category not in categories):
            industries[industry] = skillz
            categories[category] = {industry : industries[industry]}
        else:
            if (industry not in industries):
                categories[category][industry] = skillz
    return categories