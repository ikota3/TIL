# Write a Python program to calculate the sum of a list of numbers. (in recursion fashion)

def sum_of_list(numbers):
    if len(numbers) == 1:
        return numbers[0]

    return numbers[0] + sum_of_list(numbers[1:])


def main():
    numbers = [i for i in range(1, 10)]
    print(sum_of_list(numbers))


if __name__ == '__main__':
    main()
