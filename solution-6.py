#7-Static method
#Problem:-Add the static method to the car class that returns a general description of a car.

class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
    @staticmethod    
    def general_description():
        return "Cars are means of transportation"
    
my_car = Car("Tata", "Nexon")
print(my_car.general_description())
print(Car.general_description())