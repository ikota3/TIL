# Write a Python class named Circle constructed by a radius and two methods which
# will compute the area and the perimeter of a circle.

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * pi

    def get_perimeter(self):
        return self.radius * 2 * pi


def main():
    circle = Circle(10)
    print(f'Area: {circle.get_area():.0f}')
    print(f'Perimeter: {circle.get_perimeter():.0f}')


if __name__ == "__main__":
    main()
