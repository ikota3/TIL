# Write a Python program to generate a series of unique random numbers

import random


def show_unique_random_numbers():
    numbers = list(range(100))
    random.shuffle(numbers)
    while numbers:
        print(numbers.pop())


def main():
    show_unique_random_numbers()


if __name__ == "__main__":
    main()
