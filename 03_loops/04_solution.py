# v4. Reverse a String
# Problem: Reverse a string using a loop.

given_input_string = input("Give me a string and I will reverse it for you: ")
reversed_string = ""

for char in given_input_string:
    reversed_string = char + reversed_string
print(reversed_string)