# C++ 007

### vector

`std::vector<T>` で、`T`型の値をいくらでも保持できる

```cpp
int main()
{
    // int型を保持するvector
    std::vector<int> vi;
    // std::string型を保持するvector
    std::vector<std::string> vs;
}
```

`std::vector<T>` 自体が型であるため、以下のように入れ子にすることもできる

```cpp
int main()
{
    // int型を保持するvector型のvector
    std::vector<std::vector<int>> vvi;
}
```

`push_back` メソッドを使うことで値を追加できる  
名前の通り、最後の要素の次に要素を追加するようにしている

```cpp
int main()
{
    std::vector<int> vi;
    vi.push_back(1);
    vi.push_back(2);
    vi.push_back(3);

    // vi -> {1, 2, 3}
}
```

`size` メソッドで要素数を取得することが出来る

```cpp
int main()
{
    std::vector<int> vi;
    // vi.size(); -> 0

    vi.push_back(1);
    // vi.size(); -> 1

    vi.push_back(5);
    // vi.size(); -> 2
}
```

`at` メソッドを使うことで要素を取得できる  
要素は 0 番目から始まる

```cpp
int main()
{
    std::vector<int> vi;
    vi.push_back(15);
    vi.push_back(5);

    // 5
    std::cout << vi.at(1) << std::endl;

    // 15
    std::cout << vi.at(0) << std::endl;
}
```

`at` メソッドに与える引数は<strong>整数型ではあるが、 `int` 型ではない</strong>  
`std::size_t` 型という特殊な型である

`size` メソッドの戻り値も、 `int` 型ではなく `std::size_t` 型である

`std::size_t` 型は負数が使えない
