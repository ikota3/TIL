# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime


def main():
    name = str(input('Name: '))
    age = int(input('Age: '))
    year_of_100_years_old = 100 - age + datetime.datetime.now().year
    print(f'{name} will be 100 years old in the year {year_of_100_years_old}')


if __name__ == "__main__":
    main()
