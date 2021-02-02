# Write a Python program for sequential search.
# Sequential Search: In computer science, linear search or sequential search is a method for finding a particular value in a list
# that checks each element in sequence until the desired element is found or the list is exhausted. The list need not be ordered.


import random


def sequential_search(array, target):
    for i, v in enumerate(array):
        if v == target:
            return i


def main():
    n = 20
    shuffled_array = random.sample(range(n), n)
    target = 30
    print(f'Shuffled array: {shuffled_array}')
    print(f'Target: {target} index is {sequential_search(shuffled_array, target)}')


if __name__ == '__main__':
    main()
