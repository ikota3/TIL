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

- `npm install`

  上の一文だけで、パッケージインストール時に生成される `package-lock.json` や `package.json` のファイルから依存関係を読み取り、必要なパッケージを自動的にインストールすることが出来る  
  他のプロジェクトをクローンしたときなどに有用

### Modules

#### require

`require` を使って他のファイルを読み込むことが出来る  
`require("path")` を使うことで、そのファイルの `module.exports` で設定している値らが戻り値として返ってくる  
`{ key: value }` などのオブジェクトを登録することもできる

また、パッケージを使うときは、パッケージ名のみで指定する

```js
// world.js
const returnValue = "world";
module.exports = returnValue;
```

```js
// hello.js
const returnValue = require("./world.js"); // world
```

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

#### Express

Express は、Web アプリケーションを作成するためのフレームワーク  
これを使うことで、CRUD アプリを作ることが出来る

```js
const express = require("express");

// インスタンスを作成
const app = express();

// 設定を行う
// CSSファイルやJSファイルなどの静的なファイルを格納するフォルダを指定する
app.use(express.static("pathToStaticDirectory"));
// HBSを使用したHTML描画を行うことを指定する
app.set("view engine", "hbs");

// VIEW(HTMLやHBSなど)を置く場所
app.set("views", "pathToViewsDirectory");

// URLマッピング
// localhost:8080
app.get("", (req, res) => {
  console.log(req.query.key); // value from localhost:8080?key=value
  res.render("fileNameExcludingExtension", {
    title: "passSomethingToTheView",
  });
});

// 上で定義したlocalhost:8080以外のURLに対して以下が適用される
app.get("*", (req, res) => {
  res.send("This url is not available.");
});

// 8080でポートを開く
app.listen(8080, () => {
  console.log("Listening on localhost:8080");
});
```

#### HBS

`{{ variable }}` で変数を展開できる  
`{{>partialFileNameExcludingExtension}}` でヘッダーファイルやフッターファイルなどの変わらない表示内容を一つのファイルにし、それぞれのファイルで読み込む形にするとき、コンテンツを読み込むことが出来る  
ただ、`Partial` を使うときは、JavaScript 側で以下の設定を行わないといけない

```js
const hbs = require("hbs");

hbs.registerPartials("pathToPartialFilesDirectory");
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

## Promise

Promise は， `new Promise()` で Promise オブジェクトを作成し，引数に `resolve` と `reject` を引数に持つ Callback を設定する  
`resolve` と `reject` は実際は関数で，この関数の引数に値を与えることで，後述の `then` または `catch` に引き渡される

`resolve` は処理が成功したときに使う  
`resolve(result)` と置くだけで， Promise オブジェクトのメソッドチェーンでアクセスできる `then` からアクセスすることができる

`reject` は処理が失敗したときに使う  
`reject(error)` と置くだけで， Promise オブジェクトのメソッドチェーンでアクセスできる `catch` からアクセスすることができる

```js
// Using callback
const workCallback = (callback) => {
  setTimeout(() => {
    // callback("Error", undefined);
    callback(undefined, [1, 4, 7]);
  }, 2000);
};

workCallback((error, result) => {
  if (error) {
    return console.log(error);
  }

  console.log(`Result is ${result}`);
});

// Using promise
const workPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve([7, 4, 1]);
    reject("Error");
  }, 2000);
});

workPromise
  .then((result) => {
    console.log(`Result is ${result}`);
  })
  .catch((error) => {
    console.log(error);
  });
```

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

## Heroku

<https://devcenter.heroku.com/articles/heroku-cli#download-and-install>

- Installing on ubuntu

  ```bash
  sudo snap install --classic heroku
  ```

- Checking version

  ```bash
  heroku -v
  ```

- Logging in to heroku cli

  ```bash
  heroku login
  ```

- Adding github ssh public key to heroku

  ```bash
  heroku keys:add ~/.ssh/${filename}.pub
  ```

- Create a heroku application

  ```bash
  heroku create "applicationNameWhichIsUnique"
  ```

- Setting up stating command

  package.json(Using node)

  ```json
  {
    "scripts": {
      "start": "node src/app.js"
    }
  }
  ```

  Because of heroku running `npm run start`, you have to set up a command to `package.json`.

- Change port number

  ```js
  // heroku only for accessing PORT ENVIRONMENT variable
  const port = process.env.PORT || 8080;
  app.listen(port, () => {
    console.log(`listening on ${port}`);
  });
  ```

- Push to heroku

  ```bash
  git push heroku master
  ```

## MongoDB

### SQL and NO SQL

- SQL

  - The data is stored in a table.  
    Each data is Row and the data identifiers are called Column.
    |id|name|email|password|
    |:-:|:-:|:-:|:-:|
    |12|Tom|example@email.com|1234|

- No SQL

  - The data is stored in a Collection.  
    Each data is a Document and the data identifiers are called Field.

    ```json
    [
      {
        "id": "12",
        "name": "Tom",
        "email": "example@email.com",
        "password": "1234"
      }
    ]
    ```

### Run

- PowerScript

  ```ps1
  > C:\MongoDB\bin\mongod.exe --dbpath="C:\MongoDB_data\"
  ```

### GUI Tool

- Robo 3T
  - Checking connection
    - `db.version()`

### Setting connection

```js
// const mongodb = require("mongodb");
// const MongoClient = mongodb.MongoClient;
const { MongoClient } = require("mongodb");

// mongodb://IP_ADDRESS:PORT
const url = "mongodb://127.0.0.1:27017";

MongoClient.connect(url, { useUnifiedTopology: true }, (error, client) => {
  if (error) {
    return console.log("Unable to connect to database.");
  }

  console.log("Connected successfully.");

  const name = "test";
  const db = client.db(name);
});
```

### INSERT

```js
// insertOne (Insert one document only)
db.collection("users").insertOne(
  {
    name: "Tom",
    age: 20,
  },
  (error, result) => {
    if (error) {
      return console.log("Unable to insert user.");
    }

    // result.ops returns inserted details
    console.log(result.ops); // { name: "Tom", age: 20, id: ######### }
  }
);

// insertMany (Insert multiple document at once)
db.collection("users").insertMany(
  [
    {
      description: "desc1",
      completed: true,
    },
    {
      description: "desc2",
      completed: false,
    },
  ],
  (error, result) => {
    if (error) {
      return console.log("Unable to insert user.");
    }

    /**
     *[
     *  {
     *    description: 'desc1',
     *    completed: true,
     *    _id: 5ed8f568c95b3930ac7dc7ce
     *  },
     *  {
     *    description: 'desc2',
     *    completed: false,
     *    _id: 5ed8f568c95b3930ac7dc7cf
     *  }
     *]
     */
    console.log(result.ops);
  }
);
```

### ObjectID

MongoDB では，デフォルトで INSERT 処理が走ると Collection に Document が登録されるが，Field に`_id`という固有の Field が追加される  
これは完全に固有の値となり，従来だと連番で順番づけていたが，`_id`は競合することがない値となり、かつアクセスも早い

これをマニュアル的につけることもできる

```js
const { ObjectID } = require("mongodb");

const id = new ObjectID(); // Binary data
console.log(id.id); // <Buffer xx xx xx ... xx xx xx>
console.log(id.id.length); // 12
console.log(id.toHexString()); // xxxxxxxxxxxxxxxxxxxxxxxx
console.log(id.toHexString().length); // 24

db.collection("users").insertOne(
  {
    _id: id,
    name: "Tom",
    age: 30,
  },
  (error, result) => {
    if (error) {
      return console.log("Unable to insert user.");
    }

    console.log(result.ops); // { _id: ObjectID(xxxx..xxxx), name: "Tom", age: 30 }
  }
);
```

### SELECT (FIND)

```js
// findOne (Single document)
db.collection("users").findOne(
  {
    _id: ObjectID("5ed8fe5c42675f43e47a15d3"),
  },
  (error, result) => {
    if (error) {
      console.log("Unable to fetch from user.");
    }

    console.log(result); // { id..., name..., age... }
  }
);

// find (Multiple document)
db.collection("users")
  .find({
    age: 27,
  })
  .toArray((error, users) => {
    console.log(users); // [ { ... }, { ... } ]
  });

db.collection("users")
  .find({
    age: 27,
  })
  .count((error, count) => {
    console.log(count); // 2
  });
```

### UPDATE

```js
// Single update (Using Promise)
db.collection("users")
  .updateOne(
    {
      age: false,
    },
    {
      $set: {
        age: true,
      },
    }
  )
  .then((result) => {
    console.log(result.modifiedCount);
  })
  .catch((error) => {
    console.log(error);
  });

// Multiple update (Using Promise)
db.collection("users")
  .updateMany(
    {
      age: false,
    },
    {
      $set: {
        age: true,
      },
    }
  )
  .then((result) => {
    console.log(result.modifiedCount);
  })
  .catch((error) => {
    console.log(error);
  });
```

### DELETE

```js
// Single delete (Using Promise)
db.collection("users")
  .deleteOne({
    _id: ObjectID("5ed8f4bd3a2e7520747698ff"),
  })
  .then((result) => {
    console.log(result.deletedCount);
  })
  .catch((error) => {
    console.log(error);
  });

// Multiple delete (Using Promise)
db.collection("users")
  .deleteMany({
    age: true,
  })
  .then((result) => {
    console.log(result.deletedCount);
  })
  .catch((error) => {
    console.log(error);
  });
```

## Mongoose

### Connect

```js
const mongoose = require("mongoose");
mongoose.connect("mongodb://127.0.0.1:27017/task-manager", {
  useNewUrlParse: true,
  useUnifiedTopology: true,
});
```

### INSERT

```js
// Defining a model
const Task = mongoose.model("Task", {
  description: String,
  isCompleted: Boolean,
});

// Setting a value using the Task model
const firstTask = new Task({
  description: "This is my first task.",
  isCompleted: false,
});
// Insert. save method returns a Promise object
firstTask
  .save()
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.log(error);
  });
```
