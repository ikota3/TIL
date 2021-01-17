# Write a Python program to remove the nth index character from a nonempty string

def remove_character(text: str, n: int) -> str:
    # first approach
    # split_text = list(text)
    # del split_text[n]
    # return ''.join(split_text)

    # second approach
    first_part = text[:n]
    last_part = text[n + 1:]
    return first_part + last_part


def main():
    input_text = 'Python'
    print(remove_character(input_text, 0))


if __name__ == "__main__":
    main()
