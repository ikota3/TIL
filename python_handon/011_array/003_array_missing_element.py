# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input:
# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# Output:
# 5 is the missing number

def finder(first_array, second_array):
    missing_elements = []
    for i in first_array:
        if i not in second_array:
            missing_elements.append(i)
    return missing_elements

    # Another approach
    # This approach is for only one element
    # return(sum(first_array) - sum(second_array))


def main():
    first_array = [1, 2, 3, 4, 5, 6, 7, 8]
    second_array = [3, 7, 2, 1, 4, 6]
    missing_elements = finder(first_array, second_array)
    print(f'{", ".join(map(str, missing_elements))} is missing number.')


if __name__ == '__main__':
    main()
