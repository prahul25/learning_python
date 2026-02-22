# v10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_species_input = input("Specify your pet species: ").lower()
pet_age_input = int(input("Specify your pet age: "))

if pet_species_input == "dog":
    suggestion_for_food = f"Your {pet_species_input} needs"
    if pet_age_input < 2:
        suggestion_for_food += " Puppy dog food"
    elif pet_age_input < 5:
        suggestion_for_food += " Adult dog food"
    else:
        suggestion_for_food = "Enter valid age for dog it should be less than 5"
    print(suggestion_for_food)
elif pet_species_input == "dog":
    suggestion_for_food = f"Your {pet_species_input} needs"
    if pet_age_input < 2:
        suggestion_for_food += " Puppy cat food"
    elif pet_age_input < 5:
        suggestion_for_food += " Adult cat food"
    else:
        suggestion_for_food = "Enter valid age for cat it should be less than 5"
    print(suggestion_for_food)
else:
    print("We currently only support dogs and cats for food recommendation")
