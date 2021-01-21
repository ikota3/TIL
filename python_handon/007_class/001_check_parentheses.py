# Write a Python program to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{‌{‌{" are invalid.


class Parentheses:
    PARENTHESES_DICT = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def parentheses_is_valid(self, parentheses):
        stack = []
        for parenthese in parentheses:
            if parenthese in self.PARENTHESES_DICT:
                stack.append(parenthese)
            # if parenthese is not in the keys
            # AND (
            # the opening bracket is not in the stack
            # OR
            # parenthese is not in the values(the parenthese is not bracket)
            # )
            elif len(stack) == 0 or self.PARENTHESES_DICT[stack.pop()] != parenthese:
                return False
        # return the length of stack,
        # if the program run properly above, the stack length will be 0(=True)
        # because the second elif statement that using pop(), the half of the string will be in the stack and it will be popped
        return len(stack) == 0


def main():
    obj = Parentheses()
    input_parenteses = [
        '(){}[]',
        "()[{)}",
        "()",
        "([])",
        "{{}}"
    ]
    for parenthese in input_parenteses:
        print('valid' if obj.parentheses_is_valid(parenthese) else 'NOT valid')


if __name__ == "__main__":
    main()
