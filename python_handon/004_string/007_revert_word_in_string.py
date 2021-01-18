# 'The quick brown fox jumps over the lazy dog.'
# input : "The quick brown fox jumps over the lazy dog."
# output : "dog. lazy the over jumps fox brown quick The "

def revert_word(word: str) -> str:
    word_split = word.split()
    return ' '.join(word_split[::-1])


def main():
    input_str = 'The quick brown fox jumps over the lazy dog.'
    print(revert_word(input_str))


if __name__ == "__main__":
    main()
