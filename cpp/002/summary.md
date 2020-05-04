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

変数名は、キーワード/アンダースコアで始まる名前/アンダースコア 2 つを含む名前<strong>以外</strong>で作ることが出来る
