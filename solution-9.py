#10-MUltiple Inheritance
#Problem:-Create two classes battery and engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class Car:
    pass

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo()
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
