# V6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15
# km: Car).

distance_in_km = int(input("Give distance in km and we guide you mode of transportation: "))

distance_in_km = int(input("Give distance in km and we guide you mode of transportation: "))

if distance_in_km < 0:
    mode_of_transportation = "Invalid distance"
elif distance_in_km < 3:
    mode_of_transportation = "You can prefer walking"
elif distance_in_km < 15:
    mode_of_transportation = "You can prefer biking"
else:
    mode_of_transportation = "You can prefer using a car"

print(mode_of_transportation)