# Write a Python program to remove everything except alphanumeric characters from a string.
# Input
# '**//Python Exercises// - 12. '
# Output
# PythonExercises12

import re


def remove_everything_except_alphanumeric(text):
    # regex = re.compile(r'[a-zA-Z0-9]+')
    # return ''.join(regex.findall(text))
    regex = re.compile(r'[\W_]+')
    return regex.sub('', text)


def main():
    text = '**//Python Exercises//_ - 12. '
    removed_text = remove_everything_except_alphanumeric(text)
    print(removed_text)


if __name__ == "__main__":
    main()
