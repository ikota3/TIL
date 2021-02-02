# Write a Python program to get the factorial of a non-negative integer.


def _factorial(n, memo):
    if n == 0 or n == 1:
        return 1
    if memo[n] != -1:
        return memo[n]

    memo[n] = n * factorial(n - 1)

    return memo[n]


def factorial(n):
    memo = [-1 for _ in range(n + 1)]
    return _factorial(n, memo)


def main():
    n = 15
    print(factorial(n))


if __name__ == '__main__':
    main()
