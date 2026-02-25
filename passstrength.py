def password_strength(password):
    if len(password) < 8:
        return "Your Password length is lessthen 8.Again enter a strong Password "

    upper = lower = digit = special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        elif ch in special_chars:
            special = True

    if upper and lower and digit and special:
        return "Strong Password"
    else:
        return "Weak Password.Try a new strong password."

pwd = input("Enter your password: ")
result = password_strength(pwd)
print(result)
