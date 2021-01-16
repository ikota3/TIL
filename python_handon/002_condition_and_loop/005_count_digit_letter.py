# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6
# Digits 2

import re


def main():
    input_word = input("string: ")
    letters = 0
    digits = 0

    # first approach
    # for char in input_word:
    #     if re.match(r'[a-zA-Z]', char):
    #         letters = letters + 1
    #     elif re.match(r'\d', char):
    #         digits = digits + 1

    # second approach
    for char in input_word:
        if char.isalpha():
            letters = letters + 1
        elif char.isnumeric():
            digits = digits + 1

    print(f'Letters: {letters}')
    print(f'Digits: {digits}')


if __name__ == "__main__":
    main()
