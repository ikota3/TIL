#  Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

def main():
    n = 10
    for i in range(n):
        print(('* ' * i).lstrip())
    for i in range(n, 0, -1):
        print(('* ' * i).lstrip())


if __name__ == "__main__":
    main()
