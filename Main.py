import xlrd
import numpy as np
import sys
import matplotlib.pyplot as plt
from Student import Student
from Employer import Employer
import GetCorpus
from gensim import corpora, models, similarities
from operator import itemgetter
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
student_corpus, student_dictionary, student_texts = GetCorpus.corpus_dictionary(students)
employer_corpus, employer_dictionary, employer_texts = GetCorpus.corpus_dictionary(jobs)

employer_tfidf = models.TfidfModel(employer_corpus)
employer_index = similarities.SparseMatrixSimilarity(employer_tfidf[employer_corpus], num_features=len(
    employer_dictionary))
test = employer_dictionary.doc2bow(student_texts[0])
sims = employer_index[employer_tfidf[test]]
sims_sorted = sorted(list(enumerate(sims)), key=itemgetter(1))
sims_sorted.reverse()
print(sims_sorted)
