# V5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book,
# Snowy - Build a snowman).

weather_input = input("Describe weather and on that basis. It will gonna decide your activity to do").lower()
# print(type(weather_input))
if weather_input == 'sunny':
    print('Go for a walk')
elif weather_input == 'rainy':
    print('Read a book')
elif weather_input == 'snowy':
    print('Build a snowman')
else:
    print("Incorrect format of weather receieved")