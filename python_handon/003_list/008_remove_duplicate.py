# Write a Python program to remove duplicates from a list.
# Input a = [10,20,30,20,10,50,60,40,80,50,40]
# Output {40, 10, 80, 50, 20, 60, 30}

def main():
    input_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

    # first approach
    print(set(input_list))

    # second approach
    # duplicate_data = []
    # for data in input_list:
    #     if data not in duplicate_data:
    #         duplicate_data.append(data)
    # print(duplicate_data)


if __name__ == "__main__":
    main()
