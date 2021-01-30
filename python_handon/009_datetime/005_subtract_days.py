# Write a Python program to subtract five days from current date

import datetime


def subtract_five_days():
    return datetime.datetime.today() - datetime.timedelta(days=5)


def main():
    print(f'Current date: {datetime.datetime.today()}')
    print(f'Subtract 5 days: {subtract_five_days()}')


if __name__ == "__main__":
    main()
