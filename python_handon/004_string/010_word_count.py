# Write a Python program to count the occurrences of each word in a given sentence
# not character, word.

def count_word_occurrences(sentence: str) -> dict[str]:
    words = sentence.split()
    result = {}
    for char in words:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def main():
    input_str = 'the quick brown fox jumps over the lazy dog.'
    word_occurrences = count_word_occurrences(input_str)
    print(word_occurrences)


if __name__ == "__main__":
    main()
