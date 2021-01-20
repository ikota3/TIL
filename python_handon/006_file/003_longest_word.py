# Write a python program to find the longest words in a file
# Using test.txt file in same folder


def find_longest_words(filename):
    longest_words = []
    with open(filename) as f:
        words = f.read().split()
        longest_len = len(max(words, key=len))
        longest_words = [
            word for word in words if len(word) == longest_len
        ]
        return longest_words


def main():
    input_file_name = 'test.txt'
    longest_words = find_longest_words(input_file_name)
    print(longest_words)


if __name__ == "__main__":
    main()
