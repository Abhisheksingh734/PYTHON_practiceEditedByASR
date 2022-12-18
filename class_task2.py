class person:
    def __init__(self):
        self.name = "shubham"
        self.age = 18
    def compareage(self,other):
        if self.age == other.age:
            return True
        else :
            return False

person1 = person()
person2 = person()
if person1.compareage(person2):
    print("They are of same age")
else :
    print("they are of different age")