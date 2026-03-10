# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating
# multiple inheritance.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model  

class Diesle_Car:
    def car_info(self):
        return "Here is diesel car info"

class Electric_Car:
    def electric_info(self):
        return "Here is electric car"
    

class New_Class(Diesle_Car, Electric_Car, Car):
    pass

new_car = New_Class("tesla","sf")
print(new_car.car_info())
print(new_car.electric_info())