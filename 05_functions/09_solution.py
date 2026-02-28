# Generator Function with yield

# def even_generator(limit):
#     for i in range(2,limit + 1,2):
#         if i == limit:
#             return i
#         else:
#             print(i)

# print(even_generator(10))

def even_generator(limit):
    for i in range(2,limit + 1, 2):
        yield i

for i in even_generator(10):
    print(i)