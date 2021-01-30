# Write a Python program to get current time in milliseconds in Python

import time


def get_current_milliseconds():
    return int(round(time.time() * 1000))


def main():
    print(get_current_milliseconds())


if __name__ == "__main__":
    main()
