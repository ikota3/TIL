import math


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


if __name__ == '__main__':
    for i in range(200):
        if is_prime(i):
            print(i, end=' ')
