# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Input
# W3r@100a
# Output
# Valid password

import re


def main():
    user_input = str(input('Enter password: '))

    is_valid = False
    while True:
        if not 6 <= len(user_input) <= 16:
            break
        elif not re.search(r'[a-z]', user_input):
            break
        elif not re.search(r'[A-Z]', user_input):
            break
        elif not re.search(r'[0-9]', user_input):
            break
        elif not re.search(r'[$#@]', user_input):
            break
        else:
            is_valid = True
            break

    if is_valid:
        print('Valid password.')
    else:
        print('Not a valid password.')


if __name__ == "__main__":
    main()
