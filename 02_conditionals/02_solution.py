# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone
# gets a $2 discount on Wednesday.

todays_day = (str(input("Enter today's day: "))).lower()
user_age = int(input("Enter your age: "))

if todays_day == "wednesday":
    print("It's Wednesday! You get a $2 discount on your ticket.")
    if user_age > 18:
        print("You're movie ticket price is $10 cause you are adult")
    else:
        print("You're movie ticket price is $6 cause you are child")
else:
    if user_age > 18:
        print("You're movie ticket price is $12 cause you are adult")
    else:
        print("You're movie ticket price is $8 cause you are child")