# Write a Python program to solve the Fibonacci sequence using recursion.

def _fib(n, memo):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo[n] != -1:
        return memo[n]
    # メモを格納
    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]


def fibonacci(n):
    # 0番目と1番目の要素は使われない(ベースケースとして0または1を返しているため)
    memo = [-1 for _ in range(n + 1)]
    return _fib(n, memo)


def main():
    n = 10
    for i in range(n):
        print(fibonacci(i))


if __name__ == '__main__':
    main()
