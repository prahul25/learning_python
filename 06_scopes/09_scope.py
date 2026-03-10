# v9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

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
    
my_tesla = ElectricCar("Tesla", "Model S")
print(isinstance(my_tesla,ElectricCar))
print(isinstance(my_tesla,Car))