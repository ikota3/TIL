
# それぞれのプログラムの計算量を考えてください


# 問1 身長と体重からBMIを求める関数
# 解) O(1)
def bmi(height, weight):
    # 身長の単位を m に変換
    h = height / 100
    return weight / (h * h)


# 問2 円周率πの近似値を求める関数
# (n × n の正方形のうち、扇型の範囲内に入る数を数える)
# 解) O(n^2)
def pi(n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i * i * j <= n * n:
                cnt += 1

    # 扇型から円に変換するため4倍する
    return cnt * 4 / (n * n)


# 問3 円周率πの近似値を求める関数
# (πは4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ･･･という式で求められる)
# 解) O(n)
def pi(n):
    result = 4
    plus_minus = -1
    for i in range(1, n):
        result += plus_minus * 4 / (i * 2 - 1)
        # 符号を反転する
        plus_minus *= - 1

    return result
