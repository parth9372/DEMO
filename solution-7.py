#8-Property decoraters
#Problem:-use a property decorator in the car class to make the model attribute read only.

class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        
    def model(self):
        return self.__model
        
my_car = Car("Tata", "Nexon")
my_car.model = "Safari"
print(my_car.model)
    