# Python

## カスタムオブジェクトで with 文を使う

カスタムオブジェクトの with サポートを行うには 2 つの方法がある

以下は、リソースを取得するタイミングで、`__enter__` を呼び出し、リソースの解放時は `__exit__` を呼び出す

```python
class TestClass:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with TestClass('test.txt') as f:
    f.write('test!')
```

もう一つは、`contextlib.contextmanager` を使う方法  
ジェネレータベースのファクトリ関数を使用する

```python
from contextlib.contextmanager import contextmanager

@contextmanager
def test_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with test_file('test.txt') as f:
    f.write('test!')
```

## アンダースコア

- `_var`  
  内部で使用するということを明記する命名規則  
  ただのヒントなので、外部から使用することはできる

- `var_`  
  名前衝突を避けるための命名規則

- `__var`  
  サブクラスの名前の衝突を避けるため、名前を自動的にインタプリタが書き換えるようにしてくれる  
  <strong>ネームマングリング</strong>と呼ばれる

  例えば、`self.foo` をあるクラスで定義したとして、そのクラスを継承しているクラスで`self.foo`を定義すると、オーバライドされてしまうため、書き換えたくない変数やメソッドがある場合は、`self.__foo`を使う  
  これは`_クラス名__foo`に自動的に変換される

  ネームマングリングは外部から見れないので、取得する際は`getter`を用意する

- `__var__`  
  Python で定義される特別なメソッド  
  `__init__` や、 `__del__`など

- `_`  
   使わない変数のときに使う  
  `for _ in range(10)` で添え字を使わないときなどに使える

## 文字列のフォーマット方法

- `% operator`

  ```python
  world = 'World'
  print('Hello %s' % world) # Hello World

  # 16進数で表示
  num = 15
  print('%x' % num) # f

  # 複数置換
  print('%s %x' % (world, num)) # World f

  # キーワード複数置換
  print('%(w)s %(n)x' % {'w': world, 'n': num}) # World f
  ```

- `str.format()`

  ```python
  name = 'Bob'
  print('Hello! {}'.format(name)) # Hello! Bob

  # キーワード置換
  print('Hello! {name}'.format(name=name)) # Hello! Bob
  ```

- `f-strings`

  ```python
  name = 'Bob'
  print(f'Hello! {name}') # Hello! Bob

  x = 10
  y = 15
  print(f'{x + y: #x}') # 19
  ```

- `Template Strings`
  ```python
  from string import Template
  template = Template('Hello! $name')
  print(template.substitute(name='Bob')) # Hello! Bob
  ```

## 関数を変数に

Python では、関数はオブジェクトとして扱うことが出来、変数に関数を代入したり、配列に複数の関数を持たせることもできる

参照渡しではないため、定義した関数が`del`したとしても、扱うことが出来る  
`__name__` 属性自体はそのまま

```python
to_upper(text):
  return text.upper()

func = to_upper
print(func('hello')) # Hello

# ['TOM', 'BOB', 'MIKE']
print(list(map(to_upper, ['tom', 'bob', 'mike'])))
```

## 関数をネスト化

関数の中に関数を定義し、中で定義した関数を使い、戻り値にする  
下記の `hello` 関数の中に、 `world` 関数は、 `hello` 関数内部でのみ利用が可能  
外部からアクセスするには、関数自体を戻り値にしないと取得できない

```python
def hello(text):
  def world(text_):
    return text_.upper()
  return world(text)
```

条件によってこの関数を適用させる、なんていうこともできるので、便利  
ネストさせなくても出来る

```python
def speak(name):
  def hello():
    return 'Hello! ...'
  def hel():
    return 'Hel....'
  if name:
    return hello()
  return hel()
```

上記と似たような振る舞いだが、関数を作成する関数を作成することができる

```python
def make_add_func(num):
  def add(n):
    return n + num
  return add
```

例えば、`make_add_func`に`3`が渡されると、戻り値として
以下のような関数が戻り値となる

```python
# def add(n):
#   return n + 3
add_3 = make_add_func(3)

add_3(15) # 18
```

## オブジェクトを関数のように扱う

オブジェクトは関数ではないが、呼び出し可能にすることが出来る  
特殊メソッド `__call__` の実装を行うことで呼び出し可能となる  
また、`callable`メソッドで呼び出し可能か判断できる

```python
class Test:
  def __init__(self, n):
    self.n = n

  def __call__(self, x):
    return self.n + x

# インスタンスを作成 呼び出しているわけではない
test = Test(15)
# __call__呼び出し
print(test(10)) # 25

callable(test) # True
```

## ラムダ関数

ラムダ関数は実行すると、その時点で式が評価され、自動的に結果が返される

```python
# def _(x, y):
#   return x + y
add_lambda = lambda x, y: x + y
print(add_lambda(10, 20)) # 30

(lambda x, y: x + y)(10, 20) # 上と同義

tuple_ = [(1, 'd'), (2, 'b'), (3, 'a')]
# リスト中のタプル要素が一つずつxに入る
# この場合は、x[1]で文字列を取り出し、1番目の要素でソートを行う
print(sorted(tuple_, key=lambda x: x[1]))
```

## デコレータ

デコレータを使うと、関数やメソッド、クラスなどを書き換えなくても、振る舞いを拡張したり変更を容易にできるようになる

デコレータとは、<strong>別の関数をラッピングすることで、デコレートされた関数を実行する前後にコードを実行させる</strong>ことが出来るようになる

他の関数の振る舞いを拡張したり変更できるような、再利用可能なものを定義できる  
ラッピングされた関数自体は書き換える必要はなく、デコレートされたときのみ関数の振る舞いが変わる

デコレータは呼び出しが可能なオブジェクト  
デコレータ自身は呼び出し可能なオブジェクトを受け取り、別の呼び出しオブジェクトを返却する

```python
def ex_decorator(func):
  return func
```

上記では関数を受け取り、そのまま引数である関数を返す  
これを使ってデコレートするとこうなる

```python
def hello():
  return 'Hello'

greet = ex_decorator(hello)
print(greet()) # Hello
```

以下のシュガーシンタックスで省略できる

```python
@ex_decorator
def greet():
  return 'Hello'

print(greet()) # Hello
```

`@構文` で関数をデコレートすると、すぐにデコレートされる  
なので、デコレートされていない元の関数にはアクセスが難しくなる  
そこで、デコレートされていない関数も呼び出すことができるように、最初に書いた、変数に代入というやり方を明示的に行うことで、アクセスを簡単にすることが出来る

デコレータはラッパークロージャを通じて、`@構文`をつけた関数の振る舞いを変更させることが出来るので、元の関数を後から変更することはしなくてもいい  
それにより柔軟に振る舞いを変更させることが出来る

デコレータは複数付けることもできるため、これをしたあとはこれ、といったことが簡単にできる

```python
def strong(func):
    def wrapper():
        return f'<strong>{func()}</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return f'<em>{func()}</em>'
    return wrapper


@strong
@emphasis
def greet_1():
    return 'Hello!'


"""
greet_1関数の本来の戻り値 Hello! に、
strong関数、emphasis関数を適用させていくイメージ
適用する順番は下から!
Hello!
<em>Hello!</em>
<strong><em>Hello!</em></strong>
"""
print(greet_1())
```

デコレータは下から付けた順番から適用される

デコレータを使用せず、関数だけで片付けようとすると、以下のようにネストが深くなってしまう

```python
str_ = strong(emphasis(greet))
```

以下のようにデバッグ用にも使える

```python
def trace(func):
  def wrapper(*args, **kwargs):
    print(f'TRACE: calling {func.__name__}() with {args} {kwargs}')
    result = func(*args, **kwargs)
    print(f'TRACE: {func.__name__}() with {args} {kwargs} Returned {result}')


@trace
def print_key_value(key, value):
  return f'{key}: {value}'
```
