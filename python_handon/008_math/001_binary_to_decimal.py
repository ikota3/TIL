# Write a Python program to convert a binary number to decimal number.

# def binary_to_decimal(binary):
#     reversed_binary = binary[::-1]

#     result = 0
#     for i in range(len(binary)):
#         result += int(reversed_binary[i]) * (2 ** i)

#     return result


def another_solution(binary):
    binary_list = list(binary)

    result = 0
    for i in range(len(binary_list)):
        if binary_list.pop() == '1':
            result += 2 ** i

    return result


def main():
    binary = input('input: ')
    # decimal = binary_to_decimal(binary)
    decimal = another_solution(binary)
    print(f'output: {decimal}')


if __name__ == "__main__":
    main()
