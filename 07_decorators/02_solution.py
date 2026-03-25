# VProblem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function
# is called.

def debugger(func):
    def wrapper(*args,**kwargs):
        args_value = " ,".join(str(arg) for arg in args)
        kwargs_value = " ,".join(f"{key} ,{value}" for key, value in kwargs.items())
        result = func(*args,**kwargs)
        print(f"Calling from this function: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return result
    return wrapper


@debugger
def greet(name, greeting="Hello"):
    print(greeting)
    print(f"{greeting}, {name}")

greet("hey")