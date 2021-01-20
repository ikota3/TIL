# Write a Python program to read a random line from a file.
# Using test.txt

import random


def read_random_line(filename):
    with open(filename) as f:
        lines = f.readlines()
        # first approach
        # max_len_of_file = len(lines) - 1
        # random_line = random.randint(1, max_len_of_file)
        # return lines[random_line]

        # second approach
        return random.choice(lines)


def main():
    input_file_name = 'test.txt'
    print(read_random_line(input_file_name))


if __name__ == "__main__":
    main()
