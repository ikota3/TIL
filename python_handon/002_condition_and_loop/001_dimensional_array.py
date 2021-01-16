# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.
# Input
# Input number of rows: 3
# Input number of columns: 4
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

def main():
    max_row = int(input('Row: '))
    max_column = int(input('Column: '))
    # first approach
    two_dimensional_array = [
        [column * row for column in range(max_column)] for row in range(max_row)
    ]

    # second approach
    # two_dimensional_array = []
    # for row in range(max_row):
    #     sublist = []
    #     for column in range(max_column):
    #         sublist.append(row * column)
    #     two_dimensional_array.append(sublist)

    # third approach
    # two_dimensional_array = [
    #     [0 for _ in range(max_column)] for _ in range(max_row)
    # ]
    # for row in range(max_row):
    #     for column in range(max_column):
    #         two_dimensional_array[row][column] = row * column

    print(two_dimensional_array)


if __name__ == "__main__":
    main()
