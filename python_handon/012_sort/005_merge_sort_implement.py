# Write a Python program to sort a list of elements using the merge sort algorithm.
# Note: According to Wikipedia "Merge sort (also commonly spelled mergesort) is an O (n log n)
# comparison-based sorting algorithm. Most implementations produce a stable sort, which means that
# the implementation preserves the input order of equal elements in the sorted output."
# Algorithm:
# Conceptually, a merge sort works as follows :
# Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
# Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.

import random


def merge_sort(array):
    # 要素が 0 または 1 のときは、そのまま戻す
    if len(array) <= 1:
        return array

    # 真ん中の位置取得
    mid = len(array) // 2
    # 最初から真ん中までの要素を、再帰的に呼び出すことで分割させていく
    left = merge_sort(array[:mid])
    # 真ん中から最後までの要素を、再帰的に呼び出すことで分割させていく
    right = merge_sort(array[mid:])

    # 左の要素と右の要素を、マージする
    return _merge(left, right)


def _merge(left, right):
    result = []
    left_i, right_i = 0, 0

    # 左用のindex が 左のリストの長さを超えない
    # かつ
    # 右用のindex が 右のリストの長さを超えない
    # 限り処理を続ける
    while (left_i < len(left)) and (right_i < len(right)):
        if left[left_i] <= right[right_i]:
            # 左のリストの要素と右のリストの要素を比較したときに、
            # 左のほうが小さい(=含む)ときは、左の要素を結果に格納
            # 左用のindexのみをインクリメントする
            result.append(left[left_i])
            left_i += 1
        else:
            # 左のリストの要素と右のリストの要素を比較したときに、
            # 右のほうが小さいときは、右の要素を結果に格納
            # 右用のindexのみをインクリメントする
            result.append(right[right_i])
            right_i += 1

    # 左用のindex、右用のindexのどちらか一方が必ずTrueになり、片方はFalseになる
    # print(left_i < len(left), right_i < len(right))

    # 左用のindexが、まだ左のリストの長さを超えていない(見切っていない)とき
    if left_i < len(left):
        result.extend(left[left_i:])

    # 右用のindexが、まだ右のリストの長さを超えていない(見切っていない)とき
    if right_i < len(right):
        result.extend(right[right_i:])

    return result


def main():
    n = 20
    shuffled_array = random.sample(range(n), n)
    print(f'Shuffled list: {shuffled_array}')
    print(f'Sorted list:   {merge_sort(shuffled_array)}')


if __name__ == '__main__':
    main()
