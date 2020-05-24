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
