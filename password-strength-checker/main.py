from checker import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_number,
    check_special_char,
    calculate_score,
    check_common_password)
print("===== PASSWORD STRENGTH CHECKER =====")
password = input("enter your password:")
if check_length(password):
    print("password length:Valid")
else:
    print("password is too short..use at least 8 characters")
if check_uppercase(password):
    print("uppercase:found")
else:
    print("use at least one uppercase character")
if check_lowercase(password):
    print("lowercase:found")
else:
    print("use at least one lowercase character")
if check_number(password):
    print("num:found")
else:
    print("use at least one number")
if check_special_char(password):
    print("special char:found")
else:
    print("use at least one special character")
score = calculate_score(password)
print("\nPassword score:", score, "/6")
if score <= 2:
    print("Strength:Weak")
elif score <= 4:
    print("Strength:Medium")
else:
    print("Strength:Strong")
if check_common_password(password):
    print("Warning: This is a commonly used password!")
    print("Strength: Very Weak")
