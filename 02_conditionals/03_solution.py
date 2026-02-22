# v3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)

student_score_input = int(input("Hey, student you have to enter you're scores on that basis. You will be assigned Grade: "))

if student_score_input < 60:
    print("Your grade is F")
elif student_score_input < 70:
    print("Your grade is D")
elif student_score_input < 80:
    print("Your grade is C")
elif student_score_input < 90:
    print("Your grade is B")
elif student_score_input > 90 and student_score_input <= 100:
    print("Your grade is A")
else:
    print("Your score is invalid, please enter score between 0-100")