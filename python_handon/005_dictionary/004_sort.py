# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  [(3, 4), (4, 3), (1, 2), (2, 1), (0, 0)]

from enum import Enum


class Order(Enum):
    ASCENDING = 1
    DESCENDING = 2


def sort_dict_by_value(dictionary: dict, order: Order):
    # first approach
    # tmp_list = []
    # for key, value in dictionary.items():
    #     tmp_list.append([key, value])

    # for i in range(len(tmp_list)):
    #     for j in range(i, len(tmp_list)):
    #         if order == Order.ASCENDING:
    #             if tmp_list[i][1] > tmp_list[j][1]:
    #                 tmp_list[i], tmp_list[j] = tmp_list[j], tmp_list[i]
    #         elif order == Order.DESCENDING:
    #             if tmp_list[i][1] < tmp_list[j][1]:
    #                 tmp_list[i], tmp_list[j] = tmp_list[j], tmp_list[i]

    # return dict(tmp_list)

    # second approach
    if order == Order.ASCENDING:
        return sorted(dictionary.items(), key=lambda a: a[1])
    elif order == Order.DESCENDING:
        return sorted(dictionary.items(), key=lambda a: a[1], reverse=True)


def main():
    input_dictionary = {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}
    print(sort_dict_by_value(input_dictionary, Order.ASCENDING))
    print(sort_dict_by_value(input_dictionary, Order.DESCENDING))


if __name__ == "__main__":
    main()
