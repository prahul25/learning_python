# Function with *kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format
# key: value.

def print_kwargs(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}: {values}")

print_kwargs(name="Rahul", friend="Amit", office_friend="Kunjan")