# Write a Python program to remove the parenthesis area in a string.
#
# Input
# ['example (.com)', 'w3resource', 'github (.com)', 'stackoverflow (.com)']
#
# Output
# example
# w3resource
# github
# stackoverflow

import re


def remove_parenthesis(texts):

    if isinstance(texts, str):
        texts = [texts]

    result = []
    regex = re.compile(r'\(.*?\)')
    for text in texts:
        result.append(regex.sub('', text))

    return result


def main():
    input_strings = ['example (.com)', 'w3resource', 'github (.com)', 'stackoverflow (.com)']
    output_strings = remove_parenthesis(input_strings)
    for output_string in output_strings:
        print(output_string)


if __name__ == '__main__':
    main()
