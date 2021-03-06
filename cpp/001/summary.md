﻿# C++ 001

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
ヘッダーファイルが、 C++ で書かれていることを示すオプション `-x c++-header` を与える

`$ g++ -std=c++17 -Wall --pedantic-errors -x c++-header -o headerFileName.h.gch headerFileName.h`

GCC ではヘッダーファイルを扱うとき、同名の `.gch` ファイルが存在するときは、コンパイル済みヘッダーファイルとしてそれを扱い、ヘッダーファイルのコンパイル処理を省略する  
ただ、コンパイル済みヘッダーは一回のコンパイルに、一つしか使うことができないため、そのヘッダーファイルに、他のヘッダーファイルをすべて記述しなければならない

### Make コマンド

例えば、ソースファイルがコンパイル済みで、  
一つのソースファイルに依存関係がなく、それに変更があったとき、ソースファイルのみを変更し一回だけ再コンパイルを行えばいいときもあるが、  
一つのソースファイルに依存関係が複数あり、それに変更があったとき、変更があったソースファイルのみならず、他のソースファイルも再コンパイルしなければならないため、かなり手間である

そのため、数が膨大になるにつれ、依存関係が複雑になっていくため、これらを人間が把握するのは非常に困難であるし、不必要なコンパイルを行ってしまい、時間のロスになってしまう

これを解決できるものが、 `GNU Make` というビルドシステム

何千ものソースファイルから実行可能なファイルを生成したいとき  
`$ make`  
で出来る

何千ものソースファイルのうち、一つのソースファイルのみが変更され、必要な部分だけを効率よく再コンパイルしたいときも  
`$ make`  
で出来る

コンパイルと同時に実行も以下のコマンドで出来る  
`$ make run`

ソースファイルから生成されたプログラムなどのファイルを全て削除したいときは以下のコマンドで出来る  
`$ make clean`

#### 依存関係を記述する

`GNU Make` では `Makefile` というファイルに、 `ターゲット` 、 `事前要件` 、 `レシピ` という 3 つの概念で依存関係を記述する  
TAB 文字はスペースではダメで、TAB 文字でないといけない

```makefile
ターゲット: 事前要件
[TAB文字]レシピ
```

`ターゲット` は、生成されるファイル名を記述する  
`事前要件` は、ターゲットを生成するために必要なソースファイルを記述する  
`レシピ` は、ターゲットを生成するために必要な動作を記述する

`make` コマンドは、ターゲットより事前要件のタイムスタンプが若いとき、実行するようになっている

#### コメント

`#` で始まる行でコメントとして扱われる

#### 変数

`variable = something` で定義でき、使うときは、 `$(something)` で出来る

#### 自動変数

`$@` で `ターゲット` の名前を取得できる

```makefile
target: source
    echo $@ # target
```

`$<` で 最初の `事前要件` の名前を取得できる

```makefile
target: A B C D
    echo $< # A
```

`$^` で すべての `事前要件` の名前を空白区切りで取得できる

```makefile
target: A B C D
    echo $^ # A B C D
```

#### PHONY ターゲット

`PHONY ターゲット` とは、ただ `レシピ` を実行するのみを目的とした `ターゲット` のこと

`make` は、引数を付けずに実行すると、一番上に書かれたルールが実行される  
引数を指定 (`ターゲット` を指定) すると、その `レシピ` が実行され、依存関係にあるものも実行される  
だが、 `ターゲット` と同じファイル名があると `up to date` と表示されてしまい、実行されない

それを解決するものが、 `.PHONY ターゲット` という機能  
`.PHONY` の `事前要件` に、常に実行したいものを入力することで、 `ターゲット` がすでに作成されているか否に関わらず、実行されるようになる  
依存関係にあるものも実行される

```makefile
hello:
    echo "hello!"

.PHONY: hello
```

例として以下のような使い方がある  
コンパイルしたファイルの実行や、削除に使える

```makefile
hello: hello.cpp
    g++ -o $@ $<

run: hello
    ./hello

clean:
    rm -rf ./hello

.PHONY: run clean
```

以下で実行確認

```shell
$ make
g++ -o hello hello.cpp

$ ls
Makefile  hello  hello.cpp

$ make run
./hello
Hello World!

$ make clean
rm -rf ./hello

$ ls
Makefile  hello.cpp
```
