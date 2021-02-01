# Write a Python program to sort a list of elements using the insertion sort algorithm.
# Note: According to Wikipedia
# "Insertion sort is a simple sorting algorithm that builds the final sorted array (or list)
# one item at a time. It is much less efficient on large
# lists than more advanced algorithms such as quicksort, heapsort, or merge sort."

import random


def insertion_sort(input_array):
    array = input_array.copy()
    for current_index in range(len(array)):
        tmp = array[current_index]
        behind_index = current_index - 1
        while (behind_index >= 0) and (array[behind_index] > tmp):
            # 現在処理中のcurrent_index番目の要素から、後ろの要素と比較を行いながら見ていく
            # 後ろの要素と現在処理中の要素を比較したとき、
            # 現在処理中の要素のほうが小さいときは、現在処理中の要素を後ろの要素の前に移動させるために、
            # 後ろの要素を右にシフトさせる
            array[behind_index + 1] = array[behind_index]
            # ひとつ前の後ろの要素にアクセスするために、デクリメントする
            behind_index -= 1
        # 上記のwhile分でシフトを終えたら、現在処理中の要素を先頭(while文でシフトを終えた後の要素)に移動
        array[behind_index + 1] = tmp

    return array


def main():
    n = 20
    shuffled_array = random.sample(range(n), n)
    print(f'Shuffled list: {shuffled_array}')
    print(f'Sorted list:   {insertion_sort(shuffled_array)}')


if __name__ == '__main__':
    main()
