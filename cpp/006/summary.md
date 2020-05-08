# C++ 006

### ループ

#### goto 文

下記の例では、 13 と表示される

```cpp
int main()
{
    std::cout << 1;

    goto skip;

    std::cout << 2;

skip:
    std::cout << 3;
}
```

`goto文` では、`ラベル名: 処理内容;` で定義し、そのラベル名まで行くには `goto ラベル名;` で処理をスキップすることが出来る

また、下記のように自分自身のラベル名を呼び出すこともできる

```cpp
void hello()
{
    std::cout << "Hello!"s << std::endl;
}

int main()
{
loop:
    hello();
    goto loop;
}
```

#### 関数の宣言と定義

```cpp
// 宣言
void func();

// 定義
void func()
{
    std::cout << "Hello"s << std::endl;
}
```

同じ関数は一度しか宣言できないし、定義もできない

なぜ関数が宣言と定義のどちらも行える理由は、C++では名前は宣言しないと関数を呼び出せないからである  
下記がその例だ

```cpp
// 宣言
void func();

int main()
{
    func();
}

// 定義
void func()
{
    std::cout << "func called"s << std::endl;
}
```

#### while 文

```cpp
int main()
{
    while(1) {
        std::cout << "Infinite loop" << std::endl;
    }
}
```

#### for 文

```cpp
int main()
{
    for (int i = 1; i < 101; i++) {
        std::cout << i << " "s;
    }
}
```

#### do-while 文

```cpp
int main()
{
    do {
        std::cout << "just print this statement only"s;
    } while(false);
}
```

#### 再帰関数

再帰関数は自分自身を呼び出す関数のこと  
再帰関数では実行が終了したとき、呼び出し元に処理が戻るようになっているが、これは関数が呼び出し元を覚えているからである  
しかしこれは <strong>スタック</strong>と呼ばれるメモリーを消費してしまうため、呼び出し回数も無限に出来るというわけではない  
<strong>スタック</strong> には関数だけでなく、変数でも消費する
