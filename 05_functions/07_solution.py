# Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

# first way of doing this
def sum_of_all_num(*args):
    print(args)
    return sum(args)

print(sum_of_all_num(1,2,3,4,5,6,7,8,9,11))

# def sum_all(nums):
#     summed_number = 0
#     for num in nums:
#         summed_number = num + summed_number
#     return summed_number

# print(sum_all([1,2,3,4,5,6,7,8,9,11]))