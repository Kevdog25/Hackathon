import xlrd
from Student import Student
from Employer import Employer
__author__ = 'Kevin'


def loadxls(studentsfile,jobsfile):
    """Returns a list of the loaded resumes and job offers"""
    students = []
    jobs = []

    workbook = xlrd.open_workbook(studentsfile)
    sheet = workbook.sheet_by_index(0)
    for i in range(1,sheet.nrows):
        students.append(Student(sheet.row(i)))

    workbook = xlrd.open_workbook(jobsfile)
    sheet = workbook.sheet_by_index(0)
    for i in range(1,sheet.nrows):
        jobs.append(Employer(sheet.row(i)))

    return students,jobs


def countfrequency(s,f = []):
    for w in s.split(';'):
        w = w.strip(' ')
        found = False
        for item in f:
            if item[0]==w:
                item[1]+=1
                found = True
        if not found and w != '':
            f.append([w,1])

    f.sort(key = lambda x : x[1],reverse = True)
    return f


students,jobs = loadxls('DataFiles//TDA Students Test.xlsx','DataFiles//TDA Jobs Data Test.xls')

f = []
for s in students:
    f = countfrequency(s.Major,f)
    f = countfrequency(s.Minor,f)

for i in f:
    print(i)

print(len(f))
