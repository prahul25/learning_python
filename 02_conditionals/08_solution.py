# V8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)
password_input = len(input("Share your password and we check strenght: "))

if password_input < 6:
    print("Your password strength is weak")
elif password_input < 10:
    print("You password strength is medium")
else:
    print("Your passowrd strenght is strong")
