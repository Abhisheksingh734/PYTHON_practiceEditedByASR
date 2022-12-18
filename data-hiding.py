# practice of hiding data from the user
class person :
    def __init__(self,name,age):
        self.__name = name   #instead of declaring normally adding a double underscore will make it pvt
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age

person1 = person("Shubham",22)
print(person1._person__name) #this is how data hiding works