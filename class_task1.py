class person :
    def __init__(self,name1,rollno1):
        self.name1 = name1
        self.rollno1 = rollno1
    def printing(self):
        print("person's name is :",self.name1,"person's roll no. is :",self.rollno1)
person1 = person("shubham",61)
person2 = person("atul",37)
person1.printing()
person2.printing()
        