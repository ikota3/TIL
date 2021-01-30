# Write a Python class which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string in upper case.

class IOString:
    def __init__(self):
        self.string = ''

    def get_string(self):
        self.string = str(input('input: '))

    def print_string(self):
        print(f'output: {self.string.upper()}')


def main():
    get_and_print = IOString()
    get_and_print.get_string()
    get_and_print.print_string()


if __name__ == "__main__":
    main()
