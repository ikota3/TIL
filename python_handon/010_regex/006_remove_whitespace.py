# Remove all whitespaces from a string
#
# Input
# ' Python    Exercises '
# Output
# PythonExercises

import re


def remove_whitespace(text):
    return re.sub(r'\s+', '', text)


def main():
    input_text = ' Python    Exercises '
    output_text = remove_whitespace(input_text)
    print(output_text)


if __name__ == '__main__':
    main()
