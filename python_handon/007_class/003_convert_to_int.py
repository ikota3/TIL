# Write a Python class to convert a roman numeral to an integer
# Sample input
# 'MMMCMLXXXVI'
# 'MMMM'
# 'C'
# Sample output
# 3986
# 4000
# 100


class RomanConverter:

    ROMAN_NUMBERS = [
        'I', 'V', 'X', 'L', 'C', 'D', 'M',
    ]
    ARABIC_NUMBERS = [
        1, 5, 10, 50, 100, 500, 1000,
    ]
    ROMAN_ARABIC_MAPPING = dict(zip(ROMAN_NUMBERS, ARABIC_NUMBERS))

    def _roman_char_to_int(self, roman_char: str) -> int:
        return self.ROMAN_ARABIC_MAPPING[roman_char]

    def roman_to_int(self, roman_num: str) -> int:
        result = 0
        for i in range(len(roman_num)):
            if i > 0 and self._roman_char_to_int(roman_num[i]) > self._roman_char_to_int(roman_num[i - 1]):
                # i > 0 condition has to be set, because the i-1 will access backward
                # The reason of multiplied by 2, is because the number was added before current index
                result += self._roman_char_to_int(
                    roman_num[i]) - 2 * self._roman_char_to_int(roman_num[i - 1])
            else:
                result += self._roman_char_to_int(roman_num[i])
        return result


def main():
    roman_converter = RomanConverter()
    roman_numbers = [
        'MMMCMLXXXVI',
        'MMMM',
        'C',
    ]
    for roman_number in roman_numbers:
        arabic_number = roman_converter.roman_to_int(roman_number)
        print(arabic_number)


if __name__ == "__main__":
    main()
