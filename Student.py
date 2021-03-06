import XLSDataStruct
__author__ = 'Kevin'


class Student(XLSDataStruct.DataStruct):
    def __init__(self, row):
        self.Sims = None
        self.employmentDist = {}
        self.skillsDist = {}
        self.majorDist = {}

        self.Majors = self.validate(row[0],';')
        self.Minor = self.validate(row[1],',')
        self.GradDate = self.validate(row[2])
        self.Degrees = self.validate(row[3])
        self.Employment = []
        i = 1
        while i < 3*2:
            self.Employment.append([self.validate(row[3+i]), self.validate(row[4+i])])
            i += 2
        self.Skills = [self.validate(row[10]), self.validate(row[11]), self.validate(row[12])]
        self.Courses = self.validate(row[13])
        self.Projects = self.validate(row[14])

        self.makeEmploymentDist()
        self.makeSkillsDist()
        self.makeMajorDist()

    def makeEmploymentDist(self):
        for e in self.Employment:
            self.employmentDist = self.countfrequency(e[1], self.employmentDist)

    def makeSkillsDist(self):
        for s in self.Skills:
            self.skillsDist = self.countfrequency(s, self.skillsDist)

    def makeMajorDist(self):
        self.majorDist = self.countfrequency(self.Majors)
        self.majorDist = self.countfrequency(self.Minor,self.majorDist)

    def __str__(self):
        return('Major: {}\nMinor: {}\nGradDate: {}\nDegrees: {}\nEmployment: {}\nSkills: {}\nCourses: {}\nProjects: {}',
               format(self.Majors, self.Minor, self.GradDate, self.Degrees, self.Employment, self.Skills, self.Courses,
                      self.Projects))
