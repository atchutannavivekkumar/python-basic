#classes

class student ():
    def __init__(self,name, grade, subject):
        self.name = name 
        self.grade = grade
        self.subject = subject
        if self.grade >= 35:
            print(self.name, "got" ,self.grade ,"in" ,self.subject,"So he got P grade in exam")
        else:
            print(self.name, "got" ,self.grade ,"in" ,self.subject,"So he got F grade in exam")

class Enrollment:
    def __init__(self, name, grade, subject, courses, year):
        self.student = student(name, grade, subject)  # Creating a Student instance
        self.course = courses
        self.year = year
        print(self.student.name, "has enrolled in ", self.course, "in", self.year, " year")

class attendence(student):
    def __init__(self,name, grade, subject,attendancepercentage):
        super().__init__(name, grade, subject)
        self.student = student(name, grade, subject)
        self.attendancepecentage = attendancepercentage
        if   self.attendancepecentage >= 75:
            print("No condonation fee") 
        elif self.attendancepecentage < 75:
            print("Pay condonation fee of 500")
        else:
            print("invaild")
        

stname = str(input("enter the student name: "))
stmarks = int(input("Enter student marks: "))
stsubject = str(input("Enter subject name: "))

student1 = student(stname, stmarks, stsubject)   

StCourse = str(input("Enter student course: "))
stEnrollmentyear = int(input("Enter The student enrollment year to that course: "))

student2 = Enrollment(stname,stmarks,stsubject,StCourse,stEnrollmentyear)

stattendence = int(input("Enter student attendence: "))

attendence1 = attendence(stname, stmarks, stsubject,79)
