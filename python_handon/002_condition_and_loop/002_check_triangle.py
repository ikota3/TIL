# Write a Python program to check a triangle is valid or not
# 三角形の成立条件: 三辺の長さがa,b,cである三角形が存在する必要十分条件は、
# a < b + c かつ b < a + c かつ c < b + c
# 最大辺が a であれば、必要十分条件は a < b + c のみ


def main():
    a = input('辺A: ')
    b = input('辺B: ')
    c = input('辺C: ')
    all_lengths = [int(i) for i in (a, b, c)]
    max_length = max(all_lengths)
    all_lengths.remove(max_length)
    exclude_max_length = sum(all_lengths)

    if (max_length < exclude_max_length):
        print('This triangle is valid.')
    else:
        print('This triangle is not valid.')


if __name__ == "__main__":
    main()
