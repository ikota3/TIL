# Write a Python program to convert an integer to a roman numeral.
# Input 1, 4000
# Output I, MMMM

class IntegerConverter:

    ARABIC_NUMBERS = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    ROMAN_NUMBERS = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    def int_to_roman(self, number):
        result = ''
        i = 0
        while number > 0:
            # numberをARABIC_NUMBERS[i]で割ると、ARABIC_NUMBERS * 割れた数分
            for _ in range(number // self.ARABIC_NUMBERS[i]):
                number -= self.ARABIC_NUMBERS[i]
                result += self.ROMAN_NUMBERS[i]
            i += 1

        return result


def main():
    numbers = [
        1,
        4000,
        3986,
    ]
    integer_converter = IntegerConverter()
    for number in numbers:
        print(integer_converter.int_to_roman(number))


if __name__ == "__main__":
    main()
