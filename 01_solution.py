#1-basic class and objects
#Problem:-create a car with class with attributes like brand and model. then create an instance of this class.
#2-Class method and staff
#Problem:-Add a new method to the car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)

