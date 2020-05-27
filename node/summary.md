# Node

## Version

バージョン確認  
`node -v`

## REPL

REPL モードで起動  
`node`

## Run

ファイル名を指定して起動  
`node filename.js`

## Debug Mode

ファイルに `debugger` の一文を足し、  
そのうえで下記のコマンドを実行すると、`debugger` が追加されたところで処理が止まる  
`node inspect filename.js`

## NPM

- `npm init`

  npm 導入時に、最初にするコマンド  
  アプリの依存関係や名前などの詳細な情報を `package.json` という名前でファイルを作成する

- `npm i packageName`

  上記のコマンドで、任意のパッケージをローカルに落とすことが出来る  
  `i` は `install` の意味で、`install` と打ってもいい  
  `node_modules` という名前のフォルダが作成され、そこにパッケージが入る

- `npm i packageName -g`

  現在開発している物に対してだけにパッケージを使えるようにするには、`npm i packageName` が適しているが、どのようなプロジェクトに対してもこれは使えるようにしたい場合は、上記のコマンドが有用だ

* `npm install`

  上の一文だけで、パッケージインストール時に生成される `package-lock.json` や `package.json` のファイルから依存関係を読み取り、必要なパッケージを自動的にインストールすることが出来る  
  他のプロジェクトをクローンしたときなどに有用

### Modules

#### require

`require` を使って他のファイルを読み込むことが出来る  
`require("path")` を使うことで、そのファイルの `module.exports` で設定している値らが戻り値として返ってくる

```js
// world.js
const returnValue = "world";
module.exports = returnValue;
```

```js
// hello.js
const returnValue = require("./world.js"); // world
```

パッケージを使うときは、パッケージ名のみで指定する

#### FileSystem

ファイルシステムにアクセスすることが出来る  
下記は同期的に書き込む方法

```js
const fs = require("fs");

const filename = "filename.txt";
// If the file doesn't exist, create a new file and write with the content
// else, override the content in the written file
fs.writeFileSync(filename, "Something to write\n");

// Append the content to the selected file
fs.appendFileSync(filename, "Append!");
```

## JSON

- JavaScript オブジェクト -> 文字列  
  `JSON.stringify(object)`

- 文字列 -> JavaScript オブジェクト  
  `JSON.parse(object)`

```js
const book = {
  title: "Hello World",
  author: "Author Name",
};
const bookJSON = JSON.stringify(book); // JSON object to string object

const bookParse = JSON.parse(bookJSON); // String object to JSON object
```

## Arrow Function

```js
let func = function () {
  console.log("Normal function");
};
func();

func = () => {
  console.log("Arrow function");
};
func();

const obj = {
  name: "Bob",
  func: function () {
    console.log(this.name); // Bob
  },
  func1: () => {
    console.log(this.name); // undefined
  },
  func2() {
    console.log(this.name); // Bob
    const func3 = () => {
      console.log(this.name); // Bob
    };
    func3();

    const func4 = function () {
      console.log(this.name); // undefined
    };
    func4();
  },
};

obj.func();
obj.func1();
obj.func2();
```

## Object Property Shorthand and destructuring

オブジェクトを定義するとき、key を変数名と同じにしたいときは、変数名単一で定義することが出来る

```js
const name = "Tom";
const objLong = {
  name: name,
};
const objShort = {
  name,
};
```

オブジェクトのプロパティから一つずつ選択して、変数に代入するのもいいが、複数のプロパティを複数の変数に一気に代入することが出来る

```js
const name = "Tom";
const age = 26;
const sex = "Female";
const user = {
  name,
  age,
  sex,
};

const userName = user.name; // little bit long
const { name, sex } = user;
console.log(name, sex); // Tom Female

const { age: userAge } = user; // Define other name in the user property
console.log(userAge); // 26

const { hobby = "Movie" } = user; // Setting a default value for when its undefined
console.log(hobby); // Movie

// Using it in anonymous function
const func = ({ name }) => {
  console.log(name);
};
func(user); // Tom

// TypeError: Cannot destructure property `name` of 'undefined' or 'null'.
func(undefined);
func(null);

// Set default value to empty object,
// so if its undefined or null, the destructure won't be happen and the name variable will be undefined.
const funcFix = ({ name } = {}) => {
  console.log(name); // Tom
};
funcFix(undefined); // undefined
funcFix(null); // undefined
funcFix(user); // Tom
```

## Asynchronous

```js
setTimeout(() => {
  console.log('0 second.')
}, 0);

setTimeout(() => {
  console.log('2 second.')
}, 2000);

console.log("Hello");

// output
Hello
0 second.
2 second.
```

`setTimeout` は第 1 引数に実行したい関数、第 2 引数に何ミリ秒後かを記述する非同期処理関数

`2 second.`が最後に表示されているのは何となく理解はできるが、`0 second.`が直後に実行されず、なぜ `Hello` が先に実行されているか?  
関数は呼び出し時に `Call Stack` に 追加され、実行が終わったら除去されるが、`setTimeout` 関数は `Callback Queue` に入り、`Call Stack` に最初に入る `main` スタック(main 関数)が除去されるまで待ち続け、終わり次第 `Event Loop` によって `Call Stack` に追加されるようになっている  
なので、`main` スタックが終了するタイミングである、`console.log("Hello");` が終わった時点で、`setTimeout` が `Call Stack` に入り、実行された

## Design Pattern

定義した関数に、匿名関数を渡し、その関数を実行してもらう  
入力値を渡し、出力値を匿名関数に引き渡す

```js
const func = (arg, callback) => {
  // if arg is falsy
  if (!arg) {
    callback("This is not the correct arg. Try again.", undefined);
    return;
  }
  const result = something(arg);
  callback(undefined, result);
};

// This call print the errorMessage
func(false, (errorMessage, result) => {
  if (errorMessage) {
    return console.log(errorMessage);
  }
  console.log(result);
});

// This call print the result
func("argument", (errorMessage, result) => {
  if (errorMessage) {
    return console.log(errorMessage);
  }
  console.log(result);
});
```