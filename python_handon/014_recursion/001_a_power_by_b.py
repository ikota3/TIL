# Write a Python program to calculate the value of 'a' to the power 'b'.


def power(base, exp):
    # 指数が1のときは、基数を返す(ベースケース)
    # ベースケースとは、再帰的に繰り返し呼び出したとことで、
    # 最終的にたどり着く小さな問題が最終的にたどり着くようになるものを
    # ベースケースという
    if exp == 1:
        return base
    # 指数が1ではないときは、基数 * 基数 ** 指数
    if exp != 1:
        return base * power(base, exp - 1)


def main():
    base = 2
    exponential = 5
    print(power(base, exponential))


if __name__ == '__main__':
    main()
