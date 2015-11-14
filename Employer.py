import XLSDataStruct
__author__ = 'Kevin'

class Employer(XLSDataStruct.DataStruct):
    def __init__(self,row):
        self.Title = self.validate(row[0])
        self.Description = self.validate(row[1])
        self.Type = self.validate(row[2])
        self.Majors = self.validate(row[3])
        self.Qual = self.validate(row[4])

    def __str__(self):
        return 'Title: {}\nDescription: {}\nType: {}\nMajors: {}\nQualifications: {}'\
            .format(self.Title,self.Description,self.Type,self.Majors,self.Qual)



