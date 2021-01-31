# Write a Python program to sort a list of elements using the insertion sort algorithm.
# Note: According to Wikipedia
# "Insertion sort is a simple sorting algorithm that builds the final sorted array (or list)
# one item at a time. It is much less efficient on large
# lists than more advanced algorithms such as quicksort, heapsort, or merge sort."

import random


def insertion_sort(input_array):
    array = input_array.copy()
    for i in range(len(array)):
        tmp = array[i]
        j = i - 1
        while (j >= 0) and (array[j] > tmp):
            # i番目の要素から後ろを見ていく
            # 後ろの要素とi番目の要素を比較したとき、i番目の要素のほうが小さいときは、i番目の要素を後ろに移動させていく

            # 一つ上の要素(tmp)に移動
            # 右にシフトさせる
            array[j + 1] = array[j]
            # jをデクリメントする
            j -= 1
        # jには、上記のwhileでソートしたときの先頭部分のインデックスが格納される
        array[j + 1] = tmp

    return array


def main():
    n = 20
    shuffled_array = random.sample(range(n), n)
    print(f'Shuffled list: {shuffled_array}')
    print(f'Sorted list:   {insertion_sort(shuffled_array)}')


if __name__ == '__main__':
    main()
