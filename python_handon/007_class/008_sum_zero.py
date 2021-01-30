# Write a Python program to find the three elements that sum to zero from a set (array) of n real numbers.
# Input
# [-25, -10, -7, -3, 2, 4, 8, 10]
# Output
# [[-10, 2, 8], [-7, -3, 10]]

from operator import itemgetter


class SumZero:
    @staticmethod
    def get_three_elements_sum_to_zero(in_arr):

        out_arr = []

        in_arr_len = len(in_arr)
        for i in range(in_arr_len):
            for j in range(i + 1, in_arr_len):
                for k in range(j + 1, in_arr_len):
                    if sum(itemgetter(i, j, k)(in_arr)) == 0:
                        out_arr.append([
                            in_arr[i],
                            in_arr[j],
                            in_arr[k],
                        ])

        return out_arr


def main():
    in_arr = [-25, -10, -7, -3, 2, 4, 8, 10]

    sum_zero = SumZero()
    out_arr = sum_zero.get_three_elements_sum_to_zero(in_arr)
    print(out_arr)


if __name__ == "__main__":
    main()
