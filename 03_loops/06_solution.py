# v6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.
input_number = int(input("Give me number and I'll will help to find factorial: "))
factorial_num = 1
# first way to do
# for i in range(1,input_number+1):
#     factorial_num *= i
# print(factorial_num)

# second way to do

while input_number > 0:
    factorial_num *= input_number
    input_number -= 1
print(factorial_num)