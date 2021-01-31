# ---------------------------------------------------------------
# Challenge
#
# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# ---------------------------------------------------------------

def get_longest_word_without_repeating(text):
    substrings = []
    for i in range(len(text)):
        substring = ''
        counter = i
        while (counter < len(text)) and (text[counter] not in substring):
            substring += text[counter]
            counter += 1
        substrings.append(substring)
    return max(substrings, key=len)


def main():
    input_words = [
        'abcabcbb',
        'bbbbb',
        'pwwkew'
    ]

    for word in input_words:
        longest_word = get_longest_word_without_repeating(word)
        print(f'Given "{word}", the answer is "{longest_word}", which the length is {len(longest_word)}.')


if __name__ == '__main__':
    main()
