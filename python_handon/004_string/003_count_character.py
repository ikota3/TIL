# Write a Python program to count the number of characters (character frequency) in a string.
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

import collections


def main():
    input_text = 'hello....'

    # first approach
    # character_freq = collections.Counter(list(input_text))
    # print(character_freq)

    # second approach
    character_freq = {}
    for char in input_text:
        if char not in character_freq.keys():
            character_freq[char] = 1
        else:
            character_freq[char] += 1
    print(character_freq)


if __name__ == "__main__":
    main()
