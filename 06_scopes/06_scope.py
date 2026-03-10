# v6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    no_of_cars_created = 0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        # Car.no_of_cars_created += 1
        Car.no_of_cars_created = Car.no_of_cars_created + 1

car1 = Car("BMW","2 Series Gran Coupe")
car2 = Car("Audi","A4")
car3 = Car("Mercedes","Benz")
print(Car.no_of_cars_created)
