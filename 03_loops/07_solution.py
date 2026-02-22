# v7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    input_number = int(input("Enter value between 1 and 10: "))
    if 1 <= input_number <= 10:
        print("Thanks for entering number which is between 1 and 10")
        break
    else:
        print("Invalid number entered, try again")