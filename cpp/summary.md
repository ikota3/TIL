# C++

### GCC C++ コンパイラー

`$ g++ [Other option] -o OutputFileName SourceFileName.cpp`

#### コンパイラーオプション

`-std=` は、C++の規格を選択できる  
`-Wall` は、コンパイラーの警告メッセージのすべてを有効にするオプション (`Warning` と `all` で `Wall` ?)  
`--pedantic-errors` は、C++の規格を厳格に守らせることができる

### #include ディレクティブ

```cpp
#include <iostream>
```

上記は、 `iostream` ライブラリを読み込むコードであり、ヘッダーファイル `iostream` を読み込んでいる

C++の標準ライブラリを用いるには、都度 `#includeディレクティブ` を書く必要があるが、 `#include` を列挙した `ヘッダーファイル` を用意すれば、毎回書く必要はなくなる

作成した `cpp` ファイルに、 `#include headerFileName.h` と書いて読み込むこともできるが、 GCC のオプションを使うことで、常に `#include` した扱いにすることが出来る  
`$ g++ -include headerFileName.h -o outputFileName sourceFileName.cpp`

### コンパイルの時間を計測

`$ time g++ -std=c++17 -Wall --pedantic-errors -include headerFileName.h -o outputFileName sourceFileName.cpp`

プログラムで変更しないファイルをコンパイルしておくと、変更した部分のみをコンパイルすればよいので、時間の節約になる

GCC ではヘッダーファイルを事前にコンパイルする機能があり、標準ライブラリのヘッダーファイルは変更されないので、コンパイルしておいたほうがいい

事前にコンパイルしたヘッダーファイルをコンパイル済みヘッダー(`precompiled header`)という

ヘッダーファイルをコンパイル済みヘッダーにするには、以下で出来る  
ヘッダーファイルが、 C++ で書かれていることを示すオプション `-x c++header` を与える

`$ g++ -std=c++17 -Wall --pedantic-errors -x c++header -o headerFileName.h.gch headerFileName.h`

GCC ではヘッダーファイルを扱うとき、同名の `.gch` ファイルが存在するときは、コンパイル済みヘッダーファイルとしてそれを扱い、ヘッダーファイルのコンパイル処理を省略する  
ただ、コンパイル済みヘッダーは一回のコンパイルに、一つしか使うことができないため、そのヘッダーファイルに、他のヘッダーファイルをすべて記述しなければならない
