# Write a Python program to convert Year/Month/Day to Day of Year in Python

import datetime


def main():
    today = datetime.datetime.now()
    day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
    print(f'Day of year: {day_of_year}')


if __name__ == "__main__":
    main()
