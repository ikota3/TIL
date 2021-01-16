# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

def main():
    n = str(input('n: '))
    n1 = int(n)
    n2 = int(n * 2)
    n3 = int(n * 3)
    print(f'Result: {n1 + n2 + n3}')


if __name__ == "__main__":
    main()
