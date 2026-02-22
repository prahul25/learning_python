# V2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

given_input_number = int(input("Give as number and we add all even number upto n number"))

sum_of_even_numbers = 0

for i in range(1,given_input_number+1):
    if i % 2 == 0:
        print(i)
        sum_of_even_numbers += i
print(sum_of_even_numbers)