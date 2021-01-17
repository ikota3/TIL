# Write a Python program to get the frequency of the elements in a list.
# input
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# outout
# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

import collections


def main():
    my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

    # first approach
    # freq_elements = {}
    # for num in my_list:
    #     if num in freq_elements:
    #         freq_elements[num] = freq_elements[num] + 1
    #     else:
    #         freq_elements[num] = 1

    # second approach
    freq_elements = collections.Counter(my_list)

    print(freq_elements)


if __name__ == "__main__":
    main()
