# Write a Python class named Rectangle constructed by a length and width
# And a method which will compute the area of a rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


def main():
    rectangle = Rectangle(10, 35)
    rect_area = rectangle.get_area()
    print(rect_area)


if __name__ == "__main__":
    main()
