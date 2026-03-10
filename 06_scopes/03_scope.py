# 3. Inheritance

# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute
# battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name_of_car(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # self.brand = brand
        # self.model = model
        # another way to call the parent class constructor
        super().__init__(brand, model)
        # super().full_name_of_car()
        self.battery_size = battery_size

my_first_electric_car = ElectricCar("Mercedes","benz","85kWh")
print(my_first_electric_car.battery_size)
print(my_first_electric_car.full_name_of_car())