# Write a Python program to sum all the items in a list
# Example sum_list([1,2,-8])
# Return -5

def main():
    numbers = [1, 2, -8]

    # first approach
    print(sum(numbers))

    # second approach
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers = sum_of_numbers + number
    print(sum_of_numbers)


if __name__ == "__main__":
    main()
