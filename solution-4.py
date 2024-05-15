#5-Polymorphism
#Problem:-Demonstrate Polymorphism by defining a method fuel_type in both car and ElectricCar classes, but with differnece behaviors.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def fuel_type(self):
            return "Petrol or Diesel"
        
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
            return "Electric Charge"
        
my_car = ElectricCar("tata", "nexon", "40.5kwh")
print(my_car.fuel_type())

safari = Car("tata", "Safari")
print(safari.fuel_type())
        