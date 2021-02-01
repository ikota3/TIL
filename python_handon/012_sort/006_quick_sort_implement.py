# Write a Python program to sort a list of elements using the quick sort algorithm.
# Note : According to Wikipedia "Quicksort is a comparison sort, meaning that it can
# sort items of any type for which a "less-than" relation (formally, a total order) is defined.
# In efficient implementations it is not a stable sort, meaning that the relative order of equal
# sort items is not preserved. Quicksort can operate in-place on an array, requiring small additional
# amounts of memory to perform the sorting."

import random


def quick_sort(array):
    if len(array) <= 1:
        return array

    # ピボットを最初の位置に
    pivot = array[0]
    left, right, same = [], [], 0

    # ピボットより小さい要素、ピボットより大きい要素に分け、ピボットと同じデータのものはカウントしていく
    for i in array:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            # 同じデータが複数あったとき用に
            same += 1

    # ピボットより小さい要素ら、ピボットより大きい要素らを使って、再帰的に呼び出す
    left = quick_sort(left)
    right = quick_sort(right)

    # ピボットより小さい要素ら + ピボット * 同じデータの数 + ピボットより大きい要素ら
    return left + [pivot] * same + right


def main():
    n = 20
    shuffled_array = random.sample(range(n), n)
    shuffled_array = [2, 2, 1, 2, 3, 4, 3, 2]
    print(f'Shuffled list: {shuffled_array}')
    print(f'Sorted list:   {quick_sort(shuffled_array)}')


if __name__ == '__main__':
    main()
