# Write a Python script to concatenate following dictionaries to create a new one
# Input
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Output
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

from itertools import chain


def concatenate_dict(*dictionaries):
    result_dict = {}

    # first approach
    for dictionary in dictionaries:
        result_dict.update(dictionary)

    # second approach (using itertools)
    # result_dict = dict(chain.from_iterable(
    #     dictionary.items() for dictionary in dictionaries)
    # )

    return result_dict


def main():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    result_dict = concatenate_dict(dic1, dic2, dic3)

    expected_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    assert result_dict, expected_dict
    print(result_dict)


if __name__ == "__main__":
    main()
