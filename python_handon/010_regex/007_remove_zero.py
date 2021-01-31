# Write a Python program to remove leading zeros from an IP address.
# Input
# '216.08.094.196'
# Output
# 216.8.94.196

import re


def remove_leading_zero(text):
    return re.sub(r'(^0+|(?<=\.)0+)', '', text)


def main():
    input_text = '006.08.094.026'
    output_text = remove_leading_zero(input_text)
    print(output_text)


if __name__ == '__main__':
    main()
