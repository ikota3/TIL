# Write a Python function that takes a list of words and returns the length of the longest one

def find_longest_word(words: list[str]) -> str:
    longest_word_len = 0
    for word in words:
        if len(word) > longest_word_len:
            longest_word_len = len(word)
    return longest_word_len


def main():
    words = ["PHP", "Exercises", "Backend"]
    print(find_longest_word(words))


if __name__ == "__main__":
    main()
