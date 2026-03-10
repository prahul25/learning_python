# def func():
#     username = "CHAI"
#     print(username)
#     return

# username = "CHAI!!!!!"

# print(func())
# print(username)


# def chaicoder(num):
#     print(num)
#     def actual(x):
#         print(x)
#         return x ** num
#     return actual

# firstresult = chaicoder(5)
# print(firstresult)

# V1. Basic Class and Object
# Problem: Create a Car class withcattributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_first_car = Car("Mercedes","Benz")
print(my_first_car.brand)
print(my_first_car.model)