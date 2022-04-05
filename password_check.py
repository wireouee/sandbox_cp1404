"""
Description: A simple Password Checker

Name: Deqian He
"""

minimum_length = 2
maximum_length = 6


def main():
    """Check whether a given text has the correct password format"""
    menu = "Please enter a valid password\n" \
           "Your password must be between {} and {} characters, and contain:\n" \
           "\t1 or more uppercase characters\n" \
           "\t1 or more lowercase characters\n" \
           "\t1 or more numbers"
    print(menu.format(minimum_length, maximum_length))
    password = input(">")

    while not length_point(password) or not character_point(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {} character password is valid: {}".format(len(password), password))


def length_point(password):
    if minimum_length > len(password) or len(password) > maximum_length:
        return False
    else:
        return True


def character_point(password):
    character_lower = 0
    character_upper = 0
    character_digit = 0
    for character in password:
        if character.islower():
            character_lower += 1
        elif character.isupper():
            character_upper += 1
        elif character.isdigit():
            character_digit += 1
    if character_lower == 0 or character_upper == 0 or character_digit == 0:
        return False
    else:
        return True


main()
