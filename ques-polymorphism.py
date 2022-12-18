# create a class for a vehicle 
# u have to make sub classes car bus car2 sitting capacity to be overwritten

class vehicle :
    def capacity(self):
        print("sitting capacity is 4")

class audi(vehicle):
    pass
class bmw(vehicle):
    pass
class bus(vehicle):
    def capacity(self):
        print("the sitting capacity is 40")

objaudi = audi()
objbmw = bmw()
objbus = bus()

objbmw.capacity()
objaudi.capacity()
objbus.capacity()