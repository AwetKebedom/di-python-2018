class Student():
    def __init__(self,name,iq,grade):
        self.iq = iq
        self.grade = grade
        self.name = name

    def describe(self):
        print("{} is a student in {} grade and have {} iq".format(self.name,self.grade,self.iq))

student1 = Student(name="Awet",iq="1.8",grade="20th")
student1.describe()
