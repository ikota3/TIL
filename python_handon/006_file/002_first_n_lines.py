# Write a Python program to read first n lines of a file.
# Use test.txt file

from itertools import islice


def read_first_n_line(filename, n):
    with open(filename) as f:
        for line in islice(f, n):
            print(line)


def main():
    input_file_name = 'test.txt'
    n = 2
    read_first_n_line(input_file_name, n)


if __name__ == "__main__":
    main()
