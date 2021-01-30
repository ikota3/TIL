# Write a Python program to check
# that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
#
# Input
# "ABCDEFabcdef123450"
# "*&%@#!}{"
#
# Output
# True
# False

import re


def contains_set_of_characters(string):
    regex = re.compile(r'[a-zA-Z0-9.]')
    return bool(regex.search(string))


def main():
    strings = [
        'ABCDEFabcdef123450',
        '*&%@#!}{',
    ]
    for string in strings:
        print(contains_set_of_characters(string))


if __name__ == "__main__":
    main()
