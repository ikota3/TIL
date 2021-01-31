# Given a sorted integer array without duplicates,
# return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

def get_range_summary(array):
    result = []

    i = 0
    while i < len(array):
        end = i
        while end + 1 < len(array) and \
                array[end] + 1 == array[end + 1]:
            end += 1

        if i == end:
            result.append(f'{array[i]}')
        else:
            result.append(f'{array[i]}->{array[end]}')

        i = end + 1

    return result


def main():
    input_list = [0, 1, 2, 4, 5, 7, 9, 10]
    print(get_range_summary(input_list))


if __name__ == '__main__':
    main()
