# Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

# def find_factorial(number):
#     factorial = number
#     for i in range(1, number):
#         factorial *= i
#     return factorial

# def find_factorial(num):
#     factorial = 1

#     for n in range(1,num+1):
#         factorial = factorial * n
#     return factorial

def recursive_function(n):
    if n == 0:
        return 1
    else:
        return n * recursive_function(n-1)
print(recursive_function(0))
print(recursive_function(4))
print(recursive_function(5))