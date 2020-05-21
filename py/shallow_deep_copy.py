import copy
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

b = list(a)

a.append([10, 11, 12])  # a に新しく要素を追加

a[0][0] = 'Changed'

# a に要素は追加されていて、b には追加されていない
# だが、元からあった要素を編集すると、それは両方に反映される
# 理由は、list(a)はリストの要素の中にあるリストは、コピーせずに参照しているからだ
print(a)  # [['Changed', 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(b)  # [['Changed', 2, 3], [4, 5, 6], [7, 8, 9]]


# ディープコピーを実現するには copy モジュールを使う
class Test:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'


test1 = Test('tom')
test2 = copy.copy(test1)
print(test1)
print(test2)
