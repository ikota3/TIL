# C++ 009

### 整数

#### 10 進数

普通に数字を打ち込むと 10 進数になる  
先頭に 0 を付けると 8 進数になってしまう!

```cpp
int  decimal = 9;
// int decimal = 010; This number will be octal
```

#### 8 進数

先頭に 0 を付けることで、8 進数になる  
0-7 まで使える

```cpp
int octal = 07;
```

#### 16 新数

先頭に `0x` または `0X` を付けることで、16 進数になる  
0-9、A-F まで使える

```cpp
int hexadecimal = 0xFF;
```

#### 数値を文字で区切る

`'` を使うことで、可読性を高めることが出来る

```cpp
int num = 1'000;
```

### バイト

1 バイトは 8 ビットだ  
8 ビットは 1 ビットが 8 個ある状態のことで、1 ビットでは 0 と 1 の二通りを表現できる  
なので、2 の 8 乗分=256 通りの値が表現できる  
つまり、1 バイト=256 通りの表現ということだ

```cpp
// 0が8つ -> 0
auto zero = 0b00000000;
// 1が8つ -> 255
// 2^0 + 2^1 + ... + 2^7 = 255
auto max = 0b11111111;
```

0-255、0 を含めた 256 通りの表現ができる

`0b` を付けることで、その数は 2 進数になる  
`0b11111111` の一番左の位を最上位ビット、一番右の位を最下位ビットという

正の数だけを表したいときは、上記のようにやると `0-255` までを再現できるが、  
負の数を表すにはひと手間加えないといけない

#### 符号ビット

負の数は符号付き整数を使って表すことができる  
だが、1 バイトでは 256 通りの表現しかできないので、カバーする範囲の大きさ自体は同じとなる

以下は符号付き整数で、正と負の数を表現する

```cpp
// 1
auto one = 0b0'0000001;
// -1
auto minusOne = 0b1'0000001;
```

最上位ビットで正か負を判断するフラグを置き、それをもとに下位 7 ビット文の値を正か負を決定する  
上記の場合、`-127 ~ 127` まで表現できる  
`1 ~ 127`、`-127 ~ 1`、`+0`、`-0` の 256 通りだ

```cpp
// +0
auto plusZero = 0b00000000
// -0
auto minusZero = 0b10000000
```

`+0` と `-0`も同じゼロではあるが、符号ビットが存在しているので 2 種類も存在してしまう

#### 1 の補数

1 の補数とは、負数を絶対値で 2 進数に表したときの各ビットを反転させた値のこと  
-1 を表現したいときは、1 (0b00000001) の補数(各ビットを反転した値)で、-1 (0b11111110) で表現できる

```cpp
0b00000001 // 1
0b11111110 // -1

0b00000010 // 2
0b11111101 // -2

// -1 + (-2)
    11111110
+   11111101
------------
   111111011 // 9ビットになってしまう 反転すると00000100(4)
+          1
------------
    11111100 // 8ビットにする 反転すると00000011(3)
```

-1 と -2 の足し算をすると、結果が 9 ビットになり、-4 となる  
1 の補数表現の計算では、9 ビット目が繰り上がったとき、結果に 1 を足す取り決めがある  
この結果(8 ビットの結果)に 1 を足すと、8 ビットのまま、想定通りの結果、-3 となる

- 5 + (-2)

  ```cpp
  0b00000101 // 5
  0b11111101 // -2

      00000101
  +   11111101
  ------------
  100000010
  +          1
  ------------
      00000011 // 3
  ```

1 の補数は引き算や足し算もできるので、符号ビットよりも簡単になるが、0 の表現に問題がある  
0 は `0b00000000` だが、1 の補数で表現すると、`-0` は `0b11111111` となる  
そうすると、符号ビットと同じく、`+0` と `-0` が存在することになってしまう  
なので、1 の補数 8 ビットで表現で切る範囲は `-127 ~ 127` の 256 通りとなる

この正と負の 0 を解決する方法が、<strong>2 の補数</strong>

#### 2 の補数

2 の補数表現による負数は、1 の補数表現の負数に対して、繰り上がり時に足す 1 を加えた値になる  
-1 は 1 の補数表現だと、1 (0b00000001) の各ビットを反転させた値の、-1 (0b11111110) となる  
2 の補数表現だと、1 の補数表現で表した数 (0b11111110) に 1 を加えた値になるので、 0b11111111 となる

-2 は 2 を 1 の補数表現で反転させた値 0b11111101、これに 1 を足すことで 0b11111110 となる

- -1 + (-2)

  ```cpp
      11111111
  +   11111110
  ------------
  111111101 // 9ビット目の繰り上げを無視すると、0b11111101となる
            // これが2の補数表現だと-3となる数と同一
  ```

2 の補数表現では、引き算も足し算が出来る上、0 の表現方法は一つしかない  
8 ビットでの 2 の補数表現では、`-128 ~ 127` となる

### 整数を扱う型

整数を扱う型には、符号付きと符号なしの整数型に分かれている

- 符号付き( +, -を扱える )

  - signed char
  - short int
  - int
  - long
  - long int
  - long long int

- 符号なし( -のみ扱える(0 を含める) )
  - unsigned char
  - unsigned short int
  - unsigned int
  - unsigned long int
  - unsigned long long int

#### int

```cpp
int a = 123;
auto b = 123; // int型となる

unsigned int c = 123;
auto d = 123u; // unsigned int

signed e = 123; // int
unsigned f = 123; // unsigned int
```

#### long int

int 型以上の範囲をカバーする型  
long int と書くと長いので、long と書いてもいい

```cpp
long int a = 123;
unsigned long int b = 123;

long c = 123; // long int
unsigned long d = 123; // unsigned long int

auto e = 123l; // long int
auto f = 123L; // long int
auto g = 123ul; // unsigned long int
auto h = 123lu; // unsigned long int
```

#### long long int

long int 型以上の範囲をカバーする型

```cpp
long long a = 1;
unsigned long long b = 1;

auto c = 1ll; // long long int
auto d = 1LL; // long long int
auto e = 1ull; // unsigned long long int
```

### サイズ

整数型を含む変数のサイズは、`sizeof`演算子で確認出来る  
`sizeof` には、型名や変数名をいれることで、サイズを取得できる  
`sizeof` の戻り値は、`std::size_t` の型で返す

```cpp
int main()
{
    auto print = [](std::size_t s) {
        std::cout << s << std::endl;
    };

    print(sizeof(char));
    print(sizeof(short));
    print(sizeof(int));
    print(sizeof(long));
    print(sizeof(long long));
}
```

`std::size_t` は、符号なし型で、単位はバイト

### 表現できる範囲の取得

型の表現できる値の最小値と最大値を `std::numeric_limits<T>` で取得できる  
`::min()` で最小値を、`::max()` で最大値を取得できる

```cpp
int main()
{
    // min
    std::cout << std::numeric_limits<int>::min() << std::endl;

    // max
    std::cout << std::numeric_limits<int>::max() << std::endl;
}
```