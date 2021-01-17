# Write a Python program to create a Caesar encryption
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.
# plaintext:  defend the east wall of the castle
# ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf

from string import ascii_lowercase, ascii_uppercase


def caesar_cipher(text: str, n=1) -> str:
    lower_ascii = list(ascii_lowercase)
    upper_ascii = list(ascii_uppercase)

    ciphered_text = []
    for char in text:
        if char == ' ':
            ciphered_text.append(char)
            continue

        if char in lower_ascii:
            index = lower_ascii.index(char)
            crypt_index = (index + n) % len(lower_ascii)
            ciphered_text.append(lower_ascii[crypt_index])
        elif char in upper_ascii:
            index = upper_ascii.index(char)
            crypt_index = (index + n) % len(upper_ascii)
            ciphered_text.append(upper_ascii[crypt_index])

    return ''.join(ciphered_text)


def main():
    plain_text = 'defend the east wall of the castle'
    cipher_text = caesar_cipher(plain_text)

    EXPECTED = 'efgfoe uif fbtu xbmm pg uif dbtumf'
    assert cipher_text, EXPECTED
    print(f'plain_text:\t{plain_text}')
    print(f'cipher_text:\t{cipher_text}')


if __name__ == "__main__":
    main()
