# Write a Python program to get the current time in Python.

import datetime


def main():
    # now() and today() is almost same, but now has timezone option
    # current_time = datetime.datetime.now().time()
    current_time = datetime.datetime.today().time()
    print(current_time)


if __name__ == "__main__":
    main()
