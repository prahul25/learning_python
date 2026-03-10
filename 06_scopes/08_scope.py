# v8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
my_second_car = Car("safari","nexon")
# my_second_car.model = "nexon"  # This will raise an AttributeError because the model attribute is read-only
print(my_second_car.model)