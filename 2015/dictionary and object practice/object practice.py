import datetime

class Student() :
    campus = ''
    def __init__(self, fName, lName, major = 'Undeclared',\
                 minor = 'Undeclared') :
        self.firstName = fName
        self.lastName = lName
        self.marks = {}
        self.major = major
        self.minor = minor

    def __repr__(self):
        return 'Student: ' + self.firstName + ' ' + self.lastName +\
               ', ' + self.major + ', ' + self.minor
    
    def addMark(self, subject, mark):
        if subject not in self.marks:
            self.marks[subject] = [mark]
        else:
            self.marks[subject] = self.marks[subject] + [mark]
            
    def changeMajor(self, newMajor):
        self.major = newMajor

    def changeMinor(self, newMinor):
        self.minor = newMinor

    def printReport(self):       
        print('--------------------------------------')
        print('The University of Alberta', self.campus)      
        print(datetime.datetime.now(), '\n\n')
        print(self.firstName, self.lastName)

        for key in self.marks:
            print(key, end = ' ')
            print('{:5.1f}'.format(sum(self.marks[key]) / len(self.marks[key])))
            
class AugStudent(Student):
    campus = 'Augustana Campus'

    def __repr__(self):
        return 'Augustana Student: ' + self.firstName + ' ' + self.lastName +\
               ', ' + self.major + ', ' + self.minor
    
class VisitingStudent(Student):
    country = ''
    def setCountry(self, fromWhere):
        self.country = fromWhere
        
    def printReport(self):
        super().printReport()
        print('Visiting student from ', self.country)
 
sc = Student('Santa', 'Claus', 'Global Warming', 'Flying')
sc.addMark('AUCSC 111', 100)
sc.addMark('AUCSC 111', 98)
sc.addMark('AUCSC 111', 89)
sc.addMark('AUPED 101', 65)

eb = Student('Easter', 'Bunny', 'Eggs', 'Hopping')
pp = Student('Porky', 'Pig')



