# V5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

input_string = "teeteracdacd"

for char in input_string:
    print(char)
    if input_string.count(char) == 1:
        print(f"The first non-repeated character is: {char}")
        break