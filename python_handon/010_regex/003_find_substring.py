# Write a Python program to find the occurrence and position of the substrings within a string.
#
# Input
# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
#
# Output
# Found "exercises" at 7:16
# Found "exercises" at 22:31
# Found "exercises" at 36:45

import re


def matched_positions(text, pattern):
    regex = re.compile(f'{pattern}')

    result = []
    for i in regex.finditer(text):
        result.append(i.span())
    return result


def main():
    text = 'Python exercises, PHP exercises, C# exercises'
    pattern = 'exercises'
    for matched_position in matched_positions(text, pattern):
        print(f'Found "{pattern}" at {":".join(map(str, matched_position))}')


if __name__ == "__main__":
    main()
