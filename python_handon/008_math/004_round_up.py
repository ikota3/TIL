# Write a Python function to round up a number to specified digits.

def round_up(number, n):
    return round(number, n)


def main():
    number = 123.01247
    digits = [0, 1, 2, 3]
    for digit in digits:
        print(f'{number} -> {round_up(number, digit)}')


if __name__ == "__main__":
    main()
