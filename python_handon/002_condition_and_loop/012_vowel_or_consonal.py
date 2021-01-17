# Write a Python program to check whether an alphabet is a vowel or consonant
# 母音(aiueo, y)または子音(other)

import re


def main():
    user_input = str(input('Character: '))
    if re.match(r'[aiueo]', user_input, re.IGNORECASE):
        print('Vowel.')
    elif user_input == 'y':
        print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
    else:
        print('Consonant.')


if __name__ == "__main__":
    main()
