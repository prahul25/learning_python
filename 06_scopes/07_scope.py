# v7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "cars are means of transport"

class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        return "Electricity"
    

my_petrol_car = Car("Mercedes","Benz")
# print(Car.general_description())

# decorator function exampple
def my_decorator(func):
    def wrapper():
        print('Print Before decorator')
        func()
        print("Print After decorator")
    return wrapper
@my_decorator
def hello_by_name():
    print("Hello, Rahul")



hello_by_name()

