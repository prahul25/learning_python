input_from_user = input("Give me your age, I will classify you on the basis of age:")
converted_int_input = int(input_from_user)
if converted_int_input < 13:
    print("You are child")
elif converted_int_input < 20:
    print("You are teenage")
elif converted_int_input < 60:
    print("You are adult")
else:
    print("You are senior citizen")