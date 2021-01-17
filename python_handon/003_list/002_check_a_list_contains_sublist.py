# Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output

def is_sublist(a, b):
    if b == []:
        return True

    if a == b:
        return True

    if len(a) < len(b):
        return False

    # 並び順も考慮する
    for i in range(len(a)):
        # aのi番目の要素と、bの1番目の要素が同じとき
        if a[i] == b[0]:
            # bの2番目の要素から最後の要素まで、aのi番目+indexと違う値かをチェックする
            for j in range(1, len(b)):
                if a[i + j] != b[j]:
                    return False
            return True


def main():
    a = [2, 4, 3, 5, 7]
    b = [4, 3]
    c = [3, 7]
    print(is_sublist(a, b))
    print(is_sublist(a, c))


if __name__ == "__main__":
    main()
