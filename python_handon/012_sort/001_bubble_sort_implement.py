# Write a Python program to sort a list of elements using the bubble sort algorithm.
# Note : According to Wikipedia "Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that
# repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the
# wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.
# The algorithm, which is a comparison sort, is named for the way smaller elements "bubble" to the top of the list.
# Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort.
# It can be practical if the input is usually in sort order but may occasionally have some out-of-order elements nearly
# in position.


import random


def bubble_sort(input_array):
    array = input_array.copy()
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def main():
    n = 20
    shuffled_array = random.sample(range(n), n)
    print(f'Shuffled list: {shuffled_array}')
    print(f'Sorted list:   {bubble_sort(shuffled_array)}')


if __name__ == '__main__':
    main()
