class cars:

    def __init__(self,brand,mil):
        self.brand = brand
        self.mil = mil

car1 = cars("BMW",10)
car2 = cars("mercedes",7)
print(car1.brand,car1.mil)
print(car2.brand,car2.mil)