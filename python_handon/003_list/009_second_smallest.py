# Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, 0])
# output
# -2

def main():
    numbers = [1, 2, -8, -2, -2, 0, -2]

    # first approach
    print(sorted(set(numbers))[1])

    # second approach
    # n1, n2 = float('inf'), float('inf')
    # for number in numbers:
    #     # 1番目の最小値より小さいとき、1番目の最小値に要素を、2番目の最小値に元々あった1番目の最小値を
    #     if number < n1:
    #         n1, n2 = number, n1
    #     # 2番目の最小値より小さいとき、かつ 1番目の最小値と同じ数字ではないとき、2番目の最小値に要素を
    #     elif number < n2 and n1 != number:
    #         n2 = number
    # print(n2)


if __name__ == "__main__":
    main()
