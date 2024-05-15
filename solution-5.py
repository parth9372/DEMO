#6-Class Variables
#Problem:-Add a class variable to car thaat keeps track of the number of cars created.

class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
my_car = Car("tata", "Safari")
my_car = Car("tata", "Nexon")

print(Car.total_car)