#9-Class inheritance and isinstance() function
#Problem:-Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and EelctricCar.

class Car:
  
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

my_car = Car("tata", "Nexon")

class ElectricCar:
    
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity

tesla_car = ("Tesla", "S1", "40KWH")

print(isinstance(tesla_car, Car))
print(isinstance(tesla_car, ElectricCar))
        
