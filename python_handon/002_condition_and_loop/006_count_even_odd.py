# Count the number of even and odd numbers from a series of numbers
# Input
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4
# Number of odd numbers : 5

def main():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    even_numbers = 0
    odd_numbers = 0
    for number in numbers:
        if number % 2 == 0:
            even_numbers = even_numbers + 1
        else:
            odd_numbers = odd_numbers + 1

    print(f'Number of even numbers: {even_numbers}')
    print(f'Number of odd numbers: {odd_numbers}')


if __name__ == "__main__":
    main()
