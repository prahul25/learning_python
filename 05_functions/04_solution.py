# Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math
def circle_stats(radius):
    # 3.14 * (radius ** 2)
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return round(area,2), round(circumference,2)

area, circircumference = circle_stats(3)

print(f"Circles area and circumference is {area}, {circircumference}")