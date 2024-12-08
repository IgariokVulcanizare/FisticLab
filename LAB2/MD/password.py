def check_password_strength(password):
    def has_lower(password):
        return any(char.islower() for char in password)

    def has_upper(password):
        return any(char.isupper() for char in password)

    def has_digit(password):
        return any(char.isdigit() for char in password)

    def has_special(password):
        special_chars = "~`!@#$%^&*()-_+={}[]|\\;:\"<>,./?"
        return any(char in special_chars for char in password)

    def has_no_three_repeating(password):
        for i in range(len(password) - 2):
            if password[i] == password[i + 1] == password[i + 2]:
                return False
        return True

    def has_no_consecutive_numbers(password):
        for i in range(len(password) - 1):
            if password[i].isdigit() and password[i + 1].isdigit():
                if abs(int(password[i]) - int(password[i + 1])) == 1:
                    return False
        return True

    def has_no_sequential_chars(password):
        for i in range(len(password) - 2):
            if ord(password[i + 1]) == ord(password[i]) + 1 and ord(password[i + 2]) == ord(password[i]) + 2:
                return False
        return True

    steps = 0

    if len(password) < 8:
        steps += 8 - len(password)
    elif len(password) > 20:
        steps += len(password) - 20

    if not has_lower(password):
        steps += 1
    if not has_upper(password):
        steps += 1
    if not has_digit(password):
        steps += 1
    if not has_special(password):
        steps += 1

    if not has_no_three_repeating(password):
        steps += 1
    if not has_no_consecutive_numbers(password):
        steps += 1
    if not has_no_sequential_chars(password):
        steps += 1

    if steps == 0:
        return "good"

    return steps

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    result = check_password_strength(password)
    print(f"Password strength check result: {result}")
