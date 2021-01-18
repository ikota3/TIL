# Check if a given key already exists in a dictionary
# input
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# is_key_present(5)
# is_key_present(9)
# output
# Key is present in the dictionary
# Key is not present in the dictionary


def key_is_present(dictionary, key_name):
    return key_name in dictionary


def main():
    input_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    key_names = [5, 9]
    for key_name in key_names:
        if key_is_present(input_dict, key_name):
            print('Key is present in the dictionary.')
        else:
            print('Key is not present in the dictionary.')


if __name__ == "__main__":
    main()
