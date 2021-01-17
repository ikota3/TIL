# Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'


def add_tags(tag_name: str, content: str) -> str:
    return f'<{tag_name}>{content}</{tag_name}>'


def main():
    print(add_tags('i', 'Python'))
    print(add_tags('b', 'Python Tutorial'))


if __name__ == "__main__":
    main()
