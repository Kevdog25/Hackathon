import xlrd
import numpy as np
import sys
import matplotlib.pyplot as plt
from Student import Student
from Employer import Employer
import GetCorpus
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

students,jobs = loadxls('DataFiles//TDA Students Test.xlsx','DataFiles//TDA Jobs Data Test.xls')


#print(students[20],'\n',jobs[100])
student_corpus, student_dictionary = GetCorpus.corpus_dictionary(students)
employer_corpus, employer_dictionary = GetCorpus.corpus_dictionary(jobs)

