

# 問1
# 1950年から2050年までのうるう年を出力する
def print_leap_year():
    for year in range(1950, 2051):
        if year % 4 == 0 and year % 100 != 0:
            print(year, end=' ')


# 問2
# 1868年から2020以下に対応の西暦 -> 元号変換
def year_to_era(year):
    era = 0
    result = ''
    if 1868 <= year <= 1911:
        era = year - 1868 if year - 1868 != 0 else '元'
        result = '明治%s年' % str(era)
    elif 1912 <= year <= 1925:
        era = year - 1912 if year - 1912 != 0 else '元'
        result = '大正%s年' % str(era)
    elif 1926 <= year <= 1988:
        era = year - 1926 if year - 1926 != 0 else '元'
        result = '昭和%s年' % str(era)
    elif 1989 <= year <= 2018:
        era = year - 1989 if year - 1989 != 0 else '元'
        result = '平成%s年' % str(era)
    elif 2019 <= year:
        era = year - 2019 if year - 2019 != 0 else '元'
        result = '令和%s年' % str(era)
    else:
        result = '非対応年'

    return result


if __name__ == '__main__':
    print('--うるう年--')
    print_leap_year()
    print('--西暦を元号に変換--')
    print(year_to_era(2018))
