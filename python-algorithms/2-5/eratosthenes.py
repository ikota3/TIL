import math


def get_prime(num):
    if num <= 1:
        return []
    elif num == 2:
        return [2]

    prime = [2]
    limit = int(math.sqrt(num))

    # 奇数のリストを作成
    data = [i + 1 for i in range(2, num, 2)]
    # 検索上限 > 奇数リストにある最小の数
    while limit > data[0]:
        # 素数リストに追加
        prime.append(data[0])
        # 奇数リストを再作成
        # 既存の奇数リストにある数の中で、それぞれを最小の数で割り切れない数を入れる
        data = [j for j in data if j % data[0] != 0]

    return prime + data


print(get_prime(3))
