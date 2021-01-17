# Write a Python program to change a given string to a new string where the first and last chars have been exchanged

def main():
    input_text = 'sample_text'

    # first approach
    # split_text = list(input_text)
    # tmp = split_text[0]
    # split_text[0] = split_text[len(split_text) - 1]
    # split_text[len(split_text) - 1] = tmp
    # print(''.join(split_text))

    # second approach
    output_text = input_text[-1] + input_text[1:-1] + input_text[0]
    print(output_text)


if __name__ == "__main__":
    main()
