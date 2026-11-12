COMMON_PASSWORDS = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "password123",
    "123456789",
    "111111",
    "iloveyou"
]


def check_length(password):
    if len(password) >= 8:
        return True
    else:
        return False


def check_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def check_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def check_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def check_special_char(password):
    for char in password:
        if not char.isalnum():
            return True
    return False


def calculate_score(password):
    score = 0
    if check_length(password):
        score += 1
    if len(password):
        score += 1
    if check_uppercase(password):
        score += 1
    if check_lowercase(password):
        score += 1
    if check_number(password):
        score += 1
    if check_special_char(password):
        score += 1
    return score


def check_common_password(password):
    if password.lower() in COMMON_PASSWORDS:
        return True
    else:
        return False
