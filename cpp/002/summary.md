# C++ 002

### 標準出力

`std::cout` は、標準出力を担うライブラリ  
`<<` は、 `operator <<` という演算子

```cpp
#include <iostream>

int main()
{
    // hello
    std::cout << "hello"s;
}
```

以下のように `<<` を使うこともできる

```cpp
#include <iostream>

int main()
{
    // onetwothree
    std::cout << "one"s << "two"s << "three"s;
}
```

#### 数値と文字列の結合

下記のように行うと、 `Java` のように自動キャストはされずエラーが起こる

```cpp
int main()
{
    # ERROR!
    std::cout << 1 + "234"s;
}
```

だが、下記だと成功する上、変な結果になる  
(s を取り除いた)

```cpp
int main()
{
    # 34
    std::cout << 1 + "234";
}
```

`<<` 演算子を使うと繋げることが出来る

```cpp
int main()
{
    // Integer: 123
    std::cout << "Integer: "s << 123;
}
```

### 変数

`auto` キーワードに続いて変数名、それに代入する値を書くことで変数を定義できる  
`auto variableName = someValueToAssign`

`auto` キーワードは、変数の型を初期値から推論できる

変数名は、キーワード/アンダースコアで始まる名前/アンダースコア 2 つを含む名前<strong>以外</strong>で作ることが出来る

`= someValueToAssign` の代わりに、 `(someValue)` や `{someValue}` と書いてもいい

それぞれの型、 `int`、`double`、`std::string` と書いてもいい

浮動小数点型と整数点型を、交互にどちらからも行き来させることはできるが、浮動小数点を整数に変えると、小数部は切り捨てられる  
逆に、整数を浮動小数点に変えると、値を正確に表現できる場合と出来ない場合がある(<strong>そのときはその値に近い値</strong>)

### 関数

#### ラムダ式

C++ では関数も変数として扱える!

```cpp
int main()
{
    // Define function and assign to print
    auto print = [](auto x) {
        std::cout << x << "\n"s;
    };

    // Call print function
    print(123);
    print(3.14);
    print("hello");
}
```

上記では、 `ラムダ式` と呼ばれる関数を値として書くため文法  
ラムダ式では下記のような文法を使う

- [] ラムダ式導入部
- () 引数
- {} 処理内容

何もしない関数を定義することもできる  
定義する必要ある???

```cpp
int main()
{
    auto nothing_todo = []() {};

    nothing_todo();
}
```

`operator ()` は、<strong>ラムダ式そのものに対して適用することもできる</strong>

```cpp
int main()
{
    auto f = []() {};

    // 定義した関数を呼び出し
    f();
    // その場でラムダ式を定義し、operator () で呼び出している
    []() {}();
}
```

戻り値を使いたいときは、 `return` 文で出来る

```cpp
int main()
{
    auto f = []() {
        std::cout << "f is called!\n"s;
        return 0;
        std::cout << "this sentence won't be printed";
    };

    auto result = f();
    std::cout
        << "Return value is: "s << result << "\n"s;
}
```

#### 実際の関数の定義方法

上記はラムダ式を用いて行ったが、本来あるべき関数の姿は `Java` のような言語とほぼ同じ

```cpp
int main() {}
```

上記は `main` 関数で、

- int 戻り値の型
- main 関数名
- () 引数
- {} 処理内容

を意味している

なので、下記のように定義できる

```cpp
int plus_integers(int x, int y)
{
    return x + y;
}

int plus_doubles(double x, double y)
{
    return x + y;
}

std::string plus_strings(std::string x, std::string y)
{
    return x + y;
}

int main()
{
    // 3
    std::cout << plus_integers(1, 2) << "\n"s;
    std::cout << plus_doubles(1.5, 2.5) << "\n"s;
    std::cout << plus_strings("Hello!", "World!") << "\n"s;
}
```
