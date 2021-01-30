# Write a Python program to calculate the standard deviation of the following data.
# Input
# Sample Data:  [4, 2, 5, 8, 6]
# Output
# Standard Deviation :  2.0

import math


def calculate_standard_deviation(in_data):
    mean = sum(in_data) / len(in_data)
    sum_of_deviation_squared = sum((i - mean) ** 2 for i in in_data)
    return math.sqrt(sum_of_deviation_squared / len(in_data))


def main():
    in_data = [4, 2, 5, 8, 6]
    standard_deviation = calculate_standard_deviation(in_data)
    print(standard_deviation)


if __name__ == "__main__":
    main()
