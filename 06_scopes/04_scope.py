# V4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter
# method for it.

class Car:
    def __init__(self,brand, model):
        self.__brand = brand
        self.model = model
    
    def getBrand(self):
        return self.__brand
    
    def setBrand(self, brand):
        self.__brand = brand


first_car = Car("mercedes", "benz")
print(first_car.getBrand())
first_car.setBrand("BMW")
print(first_car.getBrand())