# def func():
#     username = "CHAI"
#     print(username)
#     return

# username = "CHAI!!!!!"

# print(func())
# print(username)


def chaicoder(num):
    print(num)
    def actual(x):
        print(x)
        return x ** num
    return actual

firstresult = chaicoder(5)
print(firstresult)