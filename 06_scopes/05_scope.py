# V5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but
# with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        return "Electricity"
    

my_petrol_car = Car("Mercedes","Benz")
print(my_petrol_car.fuel_type())

my_electric_car = ElectricCar("Tata","Safari")
print(my_electric_car.fuel_type())