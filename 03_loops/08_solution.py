# V8. Prime Number Checker
# Problem: Check if a number is prime.

input_number = int(input("Give me number and I will check whether number is prime or not: "))
identifying_prime = True
if input_number > 1:
    for i in range(2,input_number):
        if (input_number % i) == 0:
            identifying_prime = False
            break
print(identifying_prime)