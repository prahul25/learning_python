# V4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe,
# Yellow - Ripe, Brown - Overripe)

fruit = str(input("Give me name of fruit")).lower()
color = str(input("Give me color of fruit and on that basis I will define thier maturity")).lower()

if fruit == 'banana':
    if color == 'green':
        print("Your fruit is Unripe")
    elif color == 'yellow':
        print("Your fruit is ripe")
    elif color == 'brown':
        print("Your fruit is overripe")
else:
    print("You must have to choose banana")