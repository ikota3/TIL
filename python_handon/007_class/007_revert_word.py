# Write a Python class to reverse a string word by word.
# Input "hello world"
# Output "world hello"

class ReverseWord:
    def __init__(self, word):
        self.word = word

    def get_reversed_word(self):
        return ' '.join(reversed(self.word.split()))


def main():
    reverse_word = ReverseWord('hello world')
    reversed_word = reverse_word.get_reversed_word()
    print(reversed_word)


if __name__ == "__main__":
    main()
