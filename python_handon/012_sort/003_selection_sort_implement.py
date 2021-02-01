# Write a Python program to sort a list of elements using the selection sort algorithm.
# Note : The selection sort improves on the bubble sort by making only one exchange for every pass through the list.

import random


def selection_sort(input_array):
    array = input_array.copy()

    # 左から右に最小値を探して、最小値を左に移動させていくイメージ

    for i in range(len(array)):
        min_index = i
        # 現在処理中のindex + 1から最後の要素まで見ていく
        # index + 1 から 最後の要素の中までの中で、最小値があるindexを探す
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        # 現在処理中のindex と 最小値があるindex を入れ替える
        array[i], array[min_index] = array[min_index], array[i]
    return array


def main():
    n = 20
    shuffled_array = random.sample(range(n), n)
    print(f'Shuffled list: {shuffled_array}')
    print(f'Sorted list:   {selection_sort(shuffled_array)}')


if __name__ == '__main__':
    main()
