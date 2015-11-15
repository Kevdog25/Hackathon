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

students,employers = loadxls('DataFiles//TDA Students Test.xlsx','DataFiles//TDA Jobs Data Test.xls')

#print(students[20],'\n',jobs[100])
student_corpus, student_dictionary, student_texts = GetCorpus.corpus_dictionary(students)
employer_corpus, employer_dictionary, employer_texts = GetCorpus.corpus_dictionary(employers)

#import numpy as np
#print(np.mean([len(x) for x in student_texts])*len(student_texts))

corpora.MmCorpus.serialize('employer_corpus.mm', employer_corpus)
mm_employers = corpora.MmCorpus('employer_corpus.mm')
lsi_employers = models.ldamodel.LdaModel(corpus=mm_employers, id2word=employer_dictionary, num_topics=5, update_every=1, chunksize=100, passes=10)
corpora.MmCorpus.serialize('student_corpus.mm', student_corpus)
mm_students = corpora.MmCorpus('student_corpus.mm')
lsi_students = models.ldamodel.LdaModel(corpus=mm_students, id2word=student_dictionary, num_topics=5, update_every=1, chunksize=100, passes=10)
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
lsi_employers.print_topics(5)
#print('\n','-'*100)
lsi_students.print_topics(5)

# student_tfidf = models.TfidfModel(student_corpus)
# student_index = similarities.SparseMatrixSimilarity(student_tfidf[student_corpus], num_features=len(
#     student_dictionary))
# for i in range(len(employers)):
#     bow = student_dictionary.doc2bow(employer_texts[i])
#     sims = sorted(list(enumerate(student_index[student_tfidf[bow]])), key=itemgetter(1),reverse = True)
#     employers[i].Sims = sims
#
# employers.sort(key = lambda x : x.Sims[0][1],reverse = True)
# print(employers[0].Sims[0],employers[len(employers)-1].Sims[0])
# bestfrquency = {}
# for i in range(int(len(employers)/4)):
#     bestfrquency = Employer.catfrequencies(employers[i].descriptionDist,bestfrquency)
#
# b = []
# for k in bestfrquency.keys():
#     b.append([k,bestfrquency[k]])
# b.sort(key = lambda x : x[1],reverse = True)
#
# worstfrquency = {}
# for i in range(int(len(employers)/4)):
#     worstfrquency = Employer.catfrequencies(employers[len(employers)-1-i].descriptionDist,worstfrquency)
# w = []
# for k in worstfrquency.keys():
#     w.append([k,worstfrquency[k]])
# w.sort(key = lambda x : x[1],reverse=True)
# print(b)
# print(w)
#
# bdif = []
# for word in b:
#     found = False
#     for otherword in w:
#         if otherword[0] == word[0]:
#             bdif.append([word[0],word[1]-otherword[1]])
#             found = True
#             break
#     if not found:
#         bdif.append(word)
# bdif.sort(key = lambda x : abs(x[1]),reverse=True)
# print(bdif)

from WordCloud import generate_wordcloud
generate_wordcloud(student_texts)
generate_wordcloud(employer_texts)