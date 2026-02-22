# v7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

coffee_size = input("Give us size of coffee which you want ").lower()
extra_shot = input("Do you prefer extra shot of espresso ").lower()

if coffee_size in ("small","medium","large"):
    message = f"Here is your {coffee_size} size coffee."
    if extra_shot == 'yes':
        message += " With \"Extra shot\" of espresso"
    print(message)
else:
    print('Invalid input')