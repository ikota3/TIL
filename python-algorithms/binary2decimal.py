
def binary_to_decimal(binary_str):
    result = 0
    for i in range(len(binary_str)):
        result += int(binary_str[i]) * (2 ** (len(binary_str) - i - 1))

    return result


if __name__ == '__main__':
    input_str = input('Enter a binary number: ')
    try:
        binary_str = str(int(input_str))
        result = binary_to_decimal(binary_str)
        print(result)
    except ValueError:
        print('Please enter a number.')
