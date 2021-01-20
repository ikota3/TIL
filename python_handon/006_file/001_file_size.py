# Write a Python program to get the file size of a plain file.
# Use test.txt file at same folder

import os


def main():
    input_file_name = 'test.txt'
    file_status = os.stat(input_file_name)
    print(file_status.st_size)


if __name__ == "__main__":
    main()
