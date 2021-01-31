# Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
# For example,
# Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
# return [[1, 10], [11, 18], [19, 22]]

from copy import deepcopy


def merge_overlapping(overlapped_list):
    _list = deepcopy(overlapped_list)

    i = 0
    while i < len(_list) - 1:
        if _list[i][1] >= _list[i + 1][0]:
            _list[i][1] = _list[i + 1][1]
            del _list[i + 1]
            i -= 1
        i += 1

    return _list


def main():
    input_list = [[1, 3], [3, 6], [5, 10], [11, 16], [15, 18], [19, 22]]
    merged_list = merge_overlapping(input_list)
    print(f'overlapped: {input_list}')
    print(f'merged:     {merged_list}')


if __name__ == '__main__':
    main()
