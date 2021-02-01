# Write a Python program to sort a list of elements using shell sort algorithm.
# Note : According to Wikipedia "Shell sort or Shell's method, is an in-place comparison sort.
# It can be seen as either a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort).
# The method starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between
# elements to be compared. Starting with far apart elements can move some out-of-place elements into position faster than
# a simple nearest neighbor exchange."

import random


def shell_sort(input_array):
    array = input_array.copy()

    gap = len(array) // 2
    while gap > 0:
        # gap から 最後までを見ていく
        for i in range(gap, len(array)):
            current_element = array[i]
            pos = i
            # pos が gap より小さくてはダメ
            # current_element が array[pos - gap](後ろにある要素)より小さいとき
            # 例えば、current_elementが4番目のとき、pos-gapは0番目
            while (pos >= gap) and (current_element < array[pos - gap]):
                array[pos] = array[pos - gap]
                # gapを引く
                # 挿入ソートでは、1を引いて後ろの要素を見ていたが、
                # 後ろの要素にアクセスするためにgapを引く
                pos -= gap
            # 後ろの要素にcurrent_element
            array[pos] = current_element
        gap //= 2

    return array


def main():
    n = 20
    shuffled_array = random.sample(range(n), n)
    print(f'Shuffled list: {shuffled_array}')
    print(f'Sorted list:   {shell_sort(shuffled_array)}')


if __name__ == '__main__':
    main()
