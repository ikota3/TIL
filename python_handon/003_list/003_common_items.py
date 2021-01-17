# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}

def main():
    color1 = "Red", "Green", "Orange", "White"
    color2 = "Black", "Green", "White", "Pink"
    print(set(color1) & set(color2))


if __name__ == "__main__":
    main()
