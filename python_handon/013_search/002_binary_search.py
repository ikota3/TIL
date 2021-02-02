# Write a Python program for binary search.
# Binary Search : In computer science, a binary search or half-interval search algorithm finds the position of a target value
# within a sorted array. The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm and
# executes in logarithmic time.


import random


def binary_search(input_array, target):

    # ソートを行う
    array = sorted(input_array)

    # 左端
    low = 0
    # 右端
    high = len(array) - 1

    while low <= high:
        # 真ん中
        mid = (low + high) // 2

        # 真ん中の値が探している値のときは、真ん中のindexを戻す
        if array[mid] == target:
            return 'Found'
        # 真ん中の値より探している値が大きいとき、右の部分にあるということ
        # なので、左端にあたるlowを真ん中+1にする
        elif array[mid] < target:
            low = mid + 1
        # 真ん中の値より探している値が小さいとき、左の部分にあるということ
        # なので、右端にあたるhighを真ん中-1にする
        else:
            high = mid - 1

    return 'Not Found'


def main():
    n = 20
    shuffled_array = random.sample(range(n), n)
    target = 13
    print(f'Shuffled array: {shuffled_array}')
    print(f'Target: {target} was {binary_search(shuffled_array, target)}')


if __name__ == '__main__':
    main()
