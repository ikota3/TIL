# Write a Python program to get the biggest number from a list.
# max_num_in_list([1, 2, -8, 0])
# return 2


def main():
    list1 = [1, 2, -8, 0]

    # first approach
    print(max(list1))

    # second approach
    max_num = list1[0]
    for i in list1:
        if i > max_num:
            max_num = i

    print(max_num)


if __name__ == "__main__":
    main()
