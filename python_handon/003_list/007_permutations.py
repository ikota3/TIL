#  Write a Python program to generate all permutations of a list in Python
# Input [1,2,3]
# Output [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

import itertools


def exclude_indices_in_list(data, indices=[]):
    return [d for i, d in enumerate(data) if i not in indices]


def main():
    input_list = [1, 2, 3]
    result = []

    # first approach
    # input_list_len = len(input_list)
    # for i in range(input_list_len):
    #     for j in range(input_list_len - 1):
    #         for k in range(input_list_len - 2):
    #             j_list = exclude_indices_in_list(input_list, [i])
    #             k_list = exclude_indices_in_list(j_list, [j])
    #             result.append(tuple([input_list[i], j_list[j], k_list[k]]))

    result = list(itertools.permutations(input_list))

    print(result)


if __name__ == "__main__":
    main()
