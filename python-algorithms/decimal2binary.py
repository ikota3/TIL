
def decimal_to_binary(decimal_number):
    result = ''
    if decimal_number == 0:
        result = 0
        return result

    while decimal_number > 0:
        result = str(decimal_number % 2) + result
        decimal_number //= 2

    return result


if __name__ == '__main__':
    input_str = input('Enter decimal number: ')
    try:
        result = decimal_to_binary(int(input_str))
        print(result)
    except ValueError:
        print('Please enter a number.')
