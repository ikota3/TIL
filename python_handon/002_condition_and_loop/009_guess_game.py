# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random


def main():
    random_number = random.randint(1, 9)
    user_guess = int(input('Guess the number: '))

    print(f'random number is {random_number}')
    if user_guess < random_number:
        print('low.')
    elif user_guess == random_number:
        print('exactly right.')
    else:
        print('high.')


if __name__ == "__main__":
    main()
