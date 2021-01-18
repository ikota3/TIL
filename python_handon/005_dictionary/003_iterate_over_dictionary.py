# Write a Python program to iterate over dictionaries using for loops.

def main():
    input_dictionary = {'x': 10, 'y': 20, 'z': 30}
    for key, value in input_dictionary.items():
        print(f'{key}: {value}')


if __name__ == "__main__":
    main()
