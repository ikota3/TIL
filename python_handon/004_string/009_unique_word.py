# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

def main():
    input_str = 'red, white, black, red, green, black'
    input_split = input_str.split(', ')
    merge_split = sorted(set(input_split))
    print(', '.join(merge_split))


if __name__ == "__main__":
    main()
