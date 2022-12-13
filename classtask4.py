class student :
    numberofsubjects = 5
    def __init__(self,mark1,mark2,mark3):
        self.web = mark1
        self.python = mark2
        self.math = mark3
    def average(self):
        self.average = (self.web+self.python+self.math)/3
        return self.average
    #class methods-----------------------------------------------------------------------------------------------------------------------------
    @classmethod
    def classmethodex(cls):
        return cls.numberofsubjects
    @staticmethod
    def staticmethodexample():
        print("this is an example of static method")
student1 = student(5,7,6)
student2 = student(3,5,6)
student3 = student(9,4,6)
print(student1.average())
print(student.classmethodex())
student.staticmethodexample()