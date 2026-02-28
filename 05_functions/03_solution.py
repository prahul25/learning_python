# Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply_two_num(num_one,num_two):
    return num_one * num_two

print(multiply_two_num(8,5))
print(multiply_two_num('a',5))
print(multiply_two_num(5,'a'))