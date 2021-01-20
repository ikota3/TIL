# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

def main():
    result = {key: key ** 2 for key in range(1, 16)}
    print(result)


if __name__ == "__main__":
    main()
