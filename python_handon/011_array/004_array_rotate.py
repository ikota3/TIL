# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3,
# the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
# Note:
# Try to come up as many solutions as you can,
# there are at least 3 different ways to solve this problem.

def shift_array(array, steps):
    result = array.copy()
    for i in range(len(array)):
        if i + steps < len(array):
            result[i + steps] = array[i]
        else:
            result[i + steps - len(result)] = array[i]
    return result


def main():
    array = [1, 2, 3, 4, 5, 6, 7]
    steps = 3
    print(shift_array(array, steps))


if __name__ == '__main__':
    main()
