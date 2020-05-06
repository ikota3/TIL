# C++ 005

### 標準入力

入力を受け付けるには、 `std::cin` を使う  
`std` が `standard` 、 `cin` が `character input` だ

`std::cout` は `operator <<` を使って値を出力していたが、 `std::cin` は `operator >>` を使って値を変数に入れるようにする

入力した際は、空白文字や改行で区切られるようになっている

```cpp
int main()
{
    // 変数xを宣言
    std::string x{};

    // 変数xに入力
    std::cin >> x;

    // 出力
    std::cout << x;
}
```

複数の変数に入れることもできる  
`hello world` と入力すると、 `x` に `hello` が、 `y` に `world` が入るようになる

```cpp
int main()
{
    std::string x{}, y{};
    std::cin >> x >> y;

    std::cout << x << ", "s << y;
}
```

```bash
$ make run file=003.cpp
g++ -std=c++17 -Wall --pedantic-errors -include ../all.h -o program 003.cpp
./program
hello world
hello, world
```

また、文字列の他にも、整数や浮動小数点、真偽値を扱うことが出来る

```cpp
int main()
{
    int i{};
    double d{};
    bool b{};

    std::cin >> i >> d >> b;
    std::cout << std::boolalpha;
    std::cout << i << d << b;
}
```

```bash
$ make run file=004.cpp
g++ -std=c++17 -Wall --pedantic-errors -include ../all.h -o program 004.cpp
./program
10 15.6 0
1015.6false
```

上記では真偽値を数値で入力したが、文字列の `true` / `false` を入力することも出来る  
`std::boolalpha` を `std::cin` に <strong>入力</strong>させれば出来るようになる

```cpp
int main()
{
    bool b{};
    std::cin >> std::boolalpha >> b;

    std::cout << std::boolalpha;
    std::cout << b;
}
```

```bash
$ make run file=005.cpp
./program
true
true
```
