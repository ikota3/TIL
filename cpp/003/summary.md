# C++ 003

### コンパイルエラー

以下の二つが主に原因で、コンパイルエラーが発生する

- 文法エラー
- 意味エラー

#### 文法エラー

文法エラーは、C++の文法に従っていないエラーのこと  
一番しがちなものは、セミコロンの打ち忘れだろう

```cpp
int main()
{
    // expected: int x = 10";"
    int x = 10
}
```

##### C++ プログラムはどうやってエラーであることを通知するのか

上にある `main` 関数では、戻り値が `int` 型であり、 何も値を返さない場合、 `return 0` したものとみなされる

`main` 関数が `0` もしくは `EXIT_SUCCESS` を返したとき、プログラムの実行が成功したことを知らせてくれる

```cpp
int main()
{
    // This program will succeed
    return EXIT_SUCCESS;
}
```

逆に実行が失敗したときは、 `main` 関数は `EXIT_FAILURE` を返すことでエラーであることを知らせてくれる  
`EXIT_FAILURE` の値自体は、 `1` である  
なので、 `return 1;` でもいい

```cpp
int main()
{
    // This program will fail
    return EXIT_FAILURE;
}
```

#### 意味エラー

意味エラーとは、ソースファイルは文法エラーには引っかからないが、意味的に間違っているコンパイルエラーのこと

下記の例だと、 `operator %` に対して不適切なオペランドである `double` 型と `double` 型と、エラーが出る  
`operator %` では、`double` をつかって計算することは出来ないからだ

```cpp
int main()
{
    // invalid operands of types ‘double’ and ‘double’ to binary ‘operator%’
    auto x = 1.0 % 1.0;
}
```
