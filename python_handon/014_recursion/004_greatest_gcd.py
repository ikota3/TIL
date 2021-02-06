# Write a Python program to find the greatest common divisor (gcd) of two integers.


def gcd(a, b):
    if a % b == 0:
        return b

    r = a % b
    return gcd(b, r)


def main():
    a = 465
    b = 360
    print(gcd(a, b))


if __name__ == '__main__':
    main()
