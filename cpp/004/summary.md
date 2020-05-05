# C++ 004

### 文

C++ では `文` が実行される  
`;` で区切られたものが `文`  
`;` だけの空の `文` も書くことが出来る

```cpp
int main()
{
    // 文
    auto x = 1 + 1;

    // 空の文
    ;
}
```

#### 複合文

これらの `文` を `{}` で囲むことで、一つの文として扱うことが出来る  
これを `複合文` という

下記がその例だ

```cpp
int main()
{
    // 複合文
    {
        std::cout << "hello!\n"s;
        std::cout << "hello!\n"s;
    }

    // これも複合文
    { std::cout << "hello!\n"s; }

    // 空の複合文
    {}
}
```

`複合文` の最後に `;` は不要

```cpp
int main()
{
    // ; は不要
    {};

    // これでいい
    {}
}
```

`複合文` のなかに `複合文` を書くこともできる

```cpp
int main()
{
    { { } }
}
```

`main` 関数の一番外側にある `{}` は `複合文` とは別のもの  
`複合文` は、複数の `文` を一纏めにしてから、一つの `文` として扱えるようにするだけの意味しかない  
ただ、 `複合文` の中で変数を宣言したとき、そのスコープ範囲は `複合文` から内側までが使える範囲となる

#### IF 文

下記のように `if` / `else if` / `else` が使える

```cpp
int main()
{
    auto x = 1;
    auto y = 2;

    if (x < y) {
        std::cout << x;
    } else if (x == y) {
        std::cout << x << ", "s << y;
    } else {
        std::cout << y;
    }
}
```

下記のように ブロック `{}` を書かなくても `true` のもののみを実行できるようにもできる

```cpp
int main()
{
    if (true) std::cout << "It's true!"s;
}
```

##### 比較演算子

| 演算子 | 意味                |
| ------ | ------------------- |
| a == b | a と b は等しい     |
| a != b | a と b は等しくない |
| a < b  | a は b より小さい   |
| a <= b | a は b 以下         |
| a > b  | a は b より大きい   |
| a >= b | a は b 以上         |

##### 条件式の値

```cpp
int main()
{
    // 1 (true)
    auto x = 1 == 1;
    // 0 (false)
    auto y = 1 != 1;
}
```

##### bool 型

下記が `bool` 型の定義方法と、出力方法だ

```cpp
int main()
{
    bool isTrue = true;
    bool isFalse = false;

    std::cout << std::boolalpha;
    std::cout << isTrue << ", "s << isFalse << "\n"s;
}
```

`bool` 型の値を出力可能にするためには、 `std::boolalpha` を `std::cout` に `operator <<` で出力しなければならない  
`std::boolalpha` 自体は何も出力しない

元に戻すためには、 `std::noboolalpha` を使う

```cpp
int main()
{
    std::cout << std::boolalpha;
    // true
    std::cout << true;

    std::cout << std::noboolalpha;
    // 0
    std::cout << false;
}
```

##### 論理否定

`!` を使えば条件を否定することができる

```cpp
int main()
{
    // trueの否定はfalseなので、0が出力される
    std::cout << !true;
}
```

##### AND 条件

`&&` を使えば AND 条件を使うことが出来る  
左の条件が `false` の場合、右は評価されない

```cpp
int main()
{
    std::cout << std::boolalpha;
    auto print = [](auto condition) {
        std::cout << condition << std::endl;
    };

    // true
    print(true && true);
    // false
    print(true && false);
    // false
    print(false && false);
    // false
    print(false && true);
}
```

##### OR 条件

`||` を使えば OR 条件を使うことが出来る  
左の評価が `true` のとき、右は評価されない

```cpp
int main()
{
    std::cout << std::boolalpha;
    auto print = [](auto condition) {
        std::cout << condition << std::endl;
    };

    // true
    print(true || true);
    // true
    print(true || false);
    // true
    print(false || true);
    // false
    print(false || false);
}
```

##### bool の四則演算

`bool` 型は `int` 型に変換できる  
`true` は `1`、 `false` は `0` なので、それに合わせて計算し表示すると下記のようになる

```cpp
int main()
{
    auto print = [](auto result) {
        std::cout << result << std::endl;
    };

    // 2
    print(true + true);
    // 1
    print(true + false);
    // 1
    print(false + true);
    // 0
    print(false + false);
}
```
