class Bird:
    def category(self):
        print("This is a category of bird")
    
    def fly(self):
        print("I can fly")


class Sparrow(Bird):
    def sizeParameter(self):
        print("i am small in size")
class Crow(Bird):
    pass
class Ostrich(Bird):
    def fly(self):
        print("I cannot fly, sorry")

objBird = Bird()
objSparrow = Sparrow()
objCrow = Crow()
objOstrich = Ostrich()

objBird.category()
objBird.fly()
objCrow.category()
objCrow.fly()
objSparrow.category()
objSparrow.fly()
objOstrich.category()
objOstrich.fly()