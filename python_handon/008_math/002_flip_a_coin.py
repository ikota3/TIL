# Write a Python program to flip a coin 1000 times and count heads and tails.

import random
from enum import Enum


class Coin(Enum):
    HEAD = 1
    TAIL = 2


def flip_coins(n):
    result = []
    for i in range(n):
        result.append(random.choice(list(Coin)))
    return result


def show_result(flipped_result):
    print(
        f'Sum of heads: {sum(1 for i in flipped_result if i == Coin.HEAD)}'
    )
    print(
        f'Sum of tails: {sum(1 for i in flipped_result if i == Coin.TAIL)}'
    )


def main():
    flipped_result = flip_coins(1000)
    show_result(flipped_result)


if __name__ == "__main__":
    main()
