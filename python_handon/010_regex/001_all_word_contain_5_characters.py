# Write a Python program to find all five characters long word in a string.
# Input
# 'The quick brown fox jumps over the lazy dog.'
# Output
# ['quick', 'brown', 'jumps']

import re


def main():
    input_str = 'The quick brown fox jumps over the lazy dog.'
    print(re.findall(r'\b\w{5}\b', input_str))


if __name__ == "__main__":
    main()
