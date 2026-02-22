# v9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

input_year = int(input("Type a year and we will check if it's a leap year: "))

#---------------------------------------------- first method
# if input_year % 400 == 0:
#     print(f"{input_year} is a leap year")
# elif input_year % 100 == 0:
#     print(f"{input_year} is NOT a leap year")
# elif input_year % 4 == 0:
#     print(f"{input_year} is a leap year")
# else:
#     print(f"{input_year} is NOT a leap year")


#---------------------------------------------- second method
if (input_year % 400 == 0) or (input_year % 4 == 0 and input_year % 100 != 0):
    print(f"Your given year {input_year} is leap year")
else:
    print(f"Your given year {input_year} is not leap year")

