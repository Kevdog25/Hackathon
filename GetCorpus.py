import Student, Employer
from gensim import corpora


def corpus_dictionary(source):
    texts = []
    if len(source) != 0 and type(source[0]) is Student.Student:
        for row in source:
            text = row.Major + row.Minor + row.Courses + row.Projects
            for p in row.Skills:
                text += p
            for p in row.Employment:
                text += p[1]
            texts.append(text)
    elif len(source) != 0 and type(source[0]) is Employer.Employer:
        for row in source:
            texts.append(row.Description + row.Majors + row.Qual)
    else:
        raise Exception

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(row) for row in texts]
    return corpus, dictionary
