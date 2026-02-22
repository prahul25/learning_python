# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

multiplication_number_upto_ten = 10
number = 3

# first approach
# for i in range(1,multiplication_number_upto_ten + 1):
#     if i != 5:
#         print(f"{number} * {i} = {number * i}")
# print(multiplication_number_upto_ten)


# second approach
for i in range(1,multiplication_number_upto_ten + 1):
    if i == 5:
        continue
    print(f"{number} * {i} = {number * i}")
print(multiplication_number_upto_ten)