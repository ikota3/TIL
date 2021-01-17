# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.(正三角形)
# An isosceles triangle is a triangle with (at least) two equal sides.(二等辺三角形)
# A scalene triangle is a triangle that has three unequal sides.(不等辺三角形)

def main():
    a = int(input('辺A: '))
    b = int(input('辺B: '))
    c = int(input('辺C: '))
    if a == b == c:
        print('Equilateral Triangle.')
    elif a != b != c:
        print('Scalene Triangle.')
    else:
        print('Isosceles Triangle.')


if __name__ == "__main__":
    main()
