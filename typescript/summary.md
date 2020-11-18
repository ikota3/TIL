# TypeScript

## Compiler options

### Compile

```bash
tsc ${filename}
```

### Compile on watch mode

```bash
tsc ${filename} -w
```

```bash
tsc ${filename} --watch
```

### Configuration file

```bash
# Make a configuration file for TypeScript
tsc --init
> message TS6071: Successfully created a tsconfig.json file.

# Compile all ts files
tsc
```

#### tsconfig.json

##### include

コンパイル対象に含める

```json
"include" :[
  "sample.ts"
]
```

##### exclude

コンパイル対象から除外する

```json
"exclude" :[
  "node_modules",
  "sample.ts",
  "**/sample.ts",
  "*.ts",
]
```

##### files

exclude でコンパイル対象から除外していても，コンパイル対象に含める

```json
"files": [
  "sample.ts"
]
```

##### compilerOptions

###### target

`es6` などのコンパイルされるバージョンを指定する．

```json
"compilerOptions": {
  "target": "es6"
}
```

###### lib

コンパイル時に，どのライブラリを使ってコンパイルを行うかを指定する．

```json
"compilerOptions": {
  "lib": [
    "ES6",
    "DOM",
    "DOM.Iterable",
    "ScriptHost"
  ]
}
```

###### allowJs

コンパイル対象に JavaScript のコードも含めるようにする．

```json
"compilerOptions": {
  "allowJs": true
}
```

###### checkJs

JavaScript のコードにエラーがないかをチェックする．

```json
"compilerOptions": {
  "checkJs": true
}
```

###### declaration, declarationMap

TypeScript の型情報を生成する．

```json
"compilerOptions": {
  "declaration": true,
  "declarationMap": true,
}
```

###### sourceMap

コンパイルされた JavaScript ファイルから，TypeScript に変換されたファイルを閲覧できるようにする．

```json
"compilerOptions": {
  "sourceMap": true
}
```

###### outDir

コンパイルした JavaScript ファイルを指定したディレクトリに配置させる．

```json
"compilerOptions": {
  "outDir": "./dist"
}
```

###### rootDir

`outDir` で指定したディレクトリにコンパイル後のファイルが格納されるが，`rootDir` を設定していない状態で行うと最も構成が少なく済む方法で出力を行う．  
そのため，複数のディレクトリにネストしてファイルが格納されていると，`outDir` で指定したディレクトリにはネストしたディレクトリは格納されず，コンパイルされたファイルだけが格納される．  
これを防ぐために `rootDir` を設定すると，ネストされたディレクトリも出力するようにできる．

```json
"compilerOptions": {
  "rootDir": "./"
}
```

###### removeComments

コメントをコンパイル時に出力するかしないかを設定する．

```json
"compilerOptions": {
  "removeComments": true
}
```

###### noEmit

TypeScript の型チェックのみを行い，何も出力しないかを設定する．

```json
"compilerOptions": {
  "noEmits": true
}
```

###### noEmitOnError

コンパイルエラーが起こったときに，コンパイルされたファイルらを出力しないようにする．

```json
"compilerOptions": {
  "noEmitOnError": true
}
```

###### downlevelIteration

ES5，ES3 で`for-of`をコンパイルするときにつけるオプション．

```json
"compilerOptions": {
  "downlevelIteration": true
}
```

###### strict

型チェックのオプションを全て有効にする．  
対象のオプションは以下．

```json
"compilerOptions": {
  "strict": true,
  "noImplicitAny": true,                 /* Raise error on expressions and declarations with an implied 'any' type. */
  "strictNullChecks": true,              /* Enable strict null checks. */
  "strictFunctionTypes": true,           /* Enable strict checking of function types. */
  "strictBindCallApply": true,           /* Enable strict 'bind', 'call', and 'apply' methods on functions. */
  "strictPropertyInitialization": true,  /* Enable strict checking of property initialization in classes. */
  "noImplicitThis": true,                /* Raise error on 'this' expressions with an implied 'any' type. */
  "alwaysStrict": true,                  /* Parse in strict mode and emit "use strict" for each source file. */
}
```

###### noUnusedLocals

使っていないローカル変数にエラーを出すようにする．

```json
"compilerOptions": {
  "noUnusedLocals": true
}
```

###### noUnusedParameters

使っていない引数にエラーを出すようにする．

```json
"compilerOptions": {
  "noUnusedParameters": true
}
```

###### noImplicitReturns

暗黙的な戻り値にエラーを出すようにする．  
全てのパターンに対して，戻り値があるように明示しなければならない．

```json
"compilerOptions": {
  "noImplicitReturns": true
}
```

## Type

### Type Annotation

#### boolean, number, string

変数名の後に、 `: 型名` と付けると、その型の変数を宣言できる  
`: 型名`は、`Type Annotation`(型注釈)と呼ばれており、省略しても型推論の機能があるためエラーにはならない

```ts
// boolean型
let isNumber: boolean = false;

// number型 小数点も含める
let number: number = 123;
let floatingNumber: number = 1.23;
let negativeFloatingNumber: number -1.23;

// string型
let str: string = "hello";
```

#### Object

```ts
const user: {
  name: string;
  age: number;
} = {
  name: "Tome",
  age: 20,
};
```

#### Array

`: 型名[]`をつけることで、その型しか入らない配列を作ることが出来る

```ts
const fruits: string[] = ["Apple", "Banana", "Grape"];
```

#### Tuple

`: [型名, 型名, ... , 型名]` とすることで、その位置の要素が、その型であることを保証する  
`push()`などで要素を追加することはできるが、その値を明示的に番号を指定して、参照することはできない  
`for`文を使って添え字変数を使うことで、参照することはできる

```ts
const bookInfo: [string, number, boolean] = ["business", 1000, false];
```

#### Enum

```ts
enum OS {
  LINUX = "linux",
  MAC = "mac",
  WINDOWS = "windows",
}

enum OSCLONE {
  LINUX, // 1
  MAC, // 2
  WINDOWS, // 3
}

const osInfo: {
  version: number;
  os: OS;
} = {
  version: 1,
  os: OS.WINDOWS,
};
console.log(osInfo); // { version: 1, os: 'windows' }

const osInfoClone: {
  version: number;
  os: OSCLONE;
} = {
  version: 1,
  os: OSCLONE.MAC,
};
console.log(osInfoClone); // { version: 1, os: 2 }
```

#### Any

どのような型も代入可能．

```ts
let anything: any = true;
anything = "string";
anything = ["1", "2", "3"];

let text = "text";
text = anything; // 代入可能
```

#### Union

`|` を使うことで，複数の型を許容することができる．

```ts
let unionType: number | string = 10;
unionType = "string";

let unionTypes: (number | string)[] = [1, "string"];
```

#### Literal

特定の値のみを許容する．

```ts
const apple: "apple" = "apple";
const bool: true = true;
const num: 1 = 1;

let clothSize: "small" | "medium" | "large" = "small";
const cloth: {
  color: string;
  size: "small" | "medium" | "large";
} = {
  color: "white",
  size: "small",
};
```

#### Type Alias

型を宣言する．

```ts
type ClothSize = "small" | "medium" | "large";
let size: ClothSize = "small";
```

#### Adding types to function

型推論の機能は，戻り値にしか効かない．  
引数はデフォルトでは `any` 型になってしまうため，戻り値はもちろん引数にも型情報をつけよう．

```ts
function add(num1: number, num2: number): number {
  return num1 + num2;
}
add(1, 2); // 3

// void
function printHello(text: string): void {
  console.log(text);
}
console.log(printHello()); // undefined
```

#### Undefined and void function

関数の戻り値がないとき，`void` 型と指定するが，`console.log()`で出力してみると，`undefined`となる．  
`undefined` 型も実はあり，指定可能と思えるが，ある時のみにしか使えない．

ただ，`void`型でどちらの場合も使えるため，`void`型で統一するほうがいいだろう．

```ts
// OK
function sayHello(name: string): void {
  console.log(`Hello! ${name}`);
}

// NG
function sayHello(name: string): undefined {
  console.log(`Hello! ${name}`);
}

// OK
function sayHello(name: string): undefined {
  return;
}
```

#### undefined and null

`undefined` と `null` 型には，`undefined` と `null` のみ代入することが可能．

```ts
let und: undefined;
und = undefined;
und = null;

let nul: null;
nul = undefined;
nul = null;
```

#### Function type

変数に関数を代入するとき，関数の引数・戻り値を指定することができる．

型推論はどちらか片一方にあれば効くため，両方で指定する必要はない．

```ts
function add(x: number, y: number): number {
  return x + y;
}

// OK
const secondAdd = add;
// OK
const firstAdd: (x: number, y: number) => number = add;
// OK
const secondAdd: (x: number, y: number) => number = function (x, y) {
  return x + y;
};

// Arrow function
const doubleNumber: (num: number) => number = (num) => num * 2;
```

#### Callback function

関数を引数にしたとき，関数の引数・戻り値の型を指定することが出来る．

```ts
function doubleAndHandle(num: number, cb: (num: number) => number): void {
  const doubledNumber = cb(num);
  console.log(doubledNumber);
}

doubleAndHandle(10, (num) => {
  return num * 2;
});
```

#### Unknown type

`unknown` は `any` 型と違い，別の変数に再代入可能にするには，型が保証されていることを確認しなければならない．

```ts
let anyInput: any;
str = anyInput; // OK

let unknownInput: unknown;
unknownInput = "text";

let str: string = "str";
str = unknownInput; // ERROR

if (typeof unknownInput === "string") {
  str = unknownInput; // OK
}
```

#### Never type

`never` は，決して何も返さないという時に使う．

```ts
function errorOccurred(message: string): never {
  throw new Error(message);
}

console.log(errorOccurred("ERR-01-01"));
```

## Class

- `public`, `constructor`, `this`

  ```ts
  class Person {
    public name: string;

    constructor(name: string) {
      this.name = name;
    }

    // thisがこのPersonオブジェクトを指しているのか
    // それとも呼び出し側のオブジェクトを指しているのかの2通り考えられ，エラーが検知されない
    greeting() {
      console.log(`Hello! My name is ${this.name}.`);
    }

    // thisの型情報を加えることで，呼び出したときにエラーであることを検知できる
    greetingWithTypeDef(this: { name: string }) {
      console.log(`Hello! My name is ${this.name}.`);
    }

    // アロー関数の場合，thisは定義時に決まるため，常に生成したインスタンスのnameが使用される
    // ただ，アロー関数はパフォーマンスが落ちるため，極力使用しない
    greetingWithArrow = () => {
      console.log(`Hello! My name is ${this.name}.`);
    };

    // thisの型情報をPersonの型のみに限定させる
    // オブジェクトにセットして呼び出すには，Personクラスの全てをセットする必要がある
    greetingWithClassTypeDef(this: Person) {
      console.log(`Hello! My name is ${this.name}.`);
    }
  }

  const person: Person = new Person("Tom");
  person.greeting(); // Hello! My name is Tom.

  // nameフィールドがない
  const secondPerson = {
    greeting: person.greeting,
  };
  secondPerson.greeting(); // Hello! My name is undefined.

  // nameフィールドを設けた
  const thirdPerson = {
    name: "Bob",
    greeting: person.greeting,
  };
  thirdPerson.greeting(); // Hello! My name is Bob.

  // 事前にエラーが検知される かつ コンパイルエラーが発生する
  // const fourthPerson = {
  //   greeting: person.greetingWithTypeDef,
  // };
  // fourthPerson.greeting();

  // nameフィールドを設けているため，エラーにならない
  const fifthPerson = {
    name: "Josh",
    greeting: person.greetingWithTypeDef,
  };
  fifthPerson.greeting(); // Hello! My name is Josh.

  // thisはPersonの型であるため，Personクラスにある全てを設けなくてはいけない
  // 全てとは，フィールド変数，メソッド
  const sixthPerson = {
    name: "Lisa",
    greeting: person.greetingWithClassTypeDef,
    greetingWithTypeDef() {},
    greetingWithArrow() {},
    greetingWithClassTypeDef() {},
  };
  sixthPerson.greeting();
  ```

- `private`

  ```ts
  class Person {
    private age: number;

    constructor(age: number) {
      this.age = age;
    }

    printAge(this: Person) {
      console.log(`My age is ${this.age}`);
    }
  }

  const person: Person = new Person(100);
  // person.age = 100000; アクセス不可
  person.printAge();
  ```

- `initialize` (sugar syntax)

  ```ts
  class Person {
    constructor(public name: string, private age: number) {}

    greeting(this: Person) {
      console.log(`name: ${this.name}, age: ${this.age}`);
    }
  }

  const person: Person = new Person("Tom", 100);
  person.greeting(); // name: Tom, age: 100
  ```

- `readonly`

  ```ts
  class Person {
    constructor(
      public readonly name: string,
      private readonly age: number,
      readonly id: number // public readonly id と同じ意味
    ) {
      // this.name = "Can Overwrite" 上書き可能
    }

    greeting(this: Person) {
      // this.name = "Cannot Overwrite"; 上書き不可
      console.log(`name: ${this.name}, age: ${this.age}`);
    }
  }

  const person: Person = new Person("Tom", 100, 123456);
  // person.name = 'Cannot Overwrite'; 上書き不可
  person.greeting(); // name: Tom, age: 100
  ```

- `extends`

  ```ts
  class Person {
    constructor(public name: string, private age: number) {}

    greeting(this: Person) {
      console.log(`name: ${this.name}, age: ${this.age}`);
    }
  }

  class Teacher extends Person {
    constructor(name: string, age: number, public subject: string) {
      super(name, age);
    }
  }

  const teacher = new Teacher("Tom", 30, "English");
  teacher.greeting(); // name: Tom, age: 30
  ```

- `protected`

  ```ts
  class Person {
    // ageをprotectedにした
    constructor(public name: string, protected age: number) {}

    greeting(this: Person) {
      console.log(`name: ${this.name}, age: ${this.age}`);
    }
  }

  class Teacher extends Person {
    constructor(name: string, age: number, public subject: string) {
      super(name, age);
    }

    greeting(this: Teacher) {
      // this.ageがアクセス可能になる
      console.log(
        `name: ${this.name}, age: ${this.age}, subject: ${this.subject}`
      );
    }
  }

  const teacher: Teacher = new Teacher("Tom", 30, "English");
  teacher.greeting(); // name: Tom, age: 30, subject: English
  ```

- `getter`, `setter`

  ```ts
  class Person {
    constructor(public _name: string) {}

    get name(): string {
      return this._name;
    }

    set name(value: string) {
      this._name = value;
    }
  }

  const person: Person = new Person("Tom");
  console.log(person.name); // Tom

  person.name = "Bob";
  console.log(person.name); // Bob
  ```

- `static`

  ```ts
  class Person {
    static species: string = "Homo sapiens";
    static isAdult(age: Number): boolean {
      if (age > 17) {
        return true;
      }

      return false;
    }

    constructor(public name: string) {}
  }

  console.log(Person.species); // Homo sapiens
  console.log(Person.isAdult(17)); // false
  ```

- `Abstract`

  ```ts
  abstract class Person {
    constructor(public name: string) {}

    greeting(this: Person) {
      console.log(`name: ${this.name}`);
      this.explainJob();
    }

    abstract explainJob(): void;
  }

  class Teacher extends Person {
    constructor(name: string, private subject: string) {
      super(name);
    }

    explainJob(): void {
      console.log(`subject: ${this.subject}`);
    }
  }

  const teacher: Teacher = new Teacher("Tom", "Math");
  teacher.greeting(); // name: Tom\nsubject: Math
  ```

- `private constructor` (Singleton)

  ```ts
  class Person {
    constructor(public name: string) {}

    greeting(this: Person) {
      console.log(`name: ${this.name}`);
    }
  }

  class Teacher extends Person {
    private static instance: Teacher;

    private constructor(name: string) {
      super(name);
    }

    static getInstance(): Teacher {
      if (Teacher.instance) {
        return Teacher.instance;
      }

      Teacher.instance = new Teacher("Tom");
      return Teacher.instance;
    }
  }

  // const teacher: Teacher = new Teacher("Tom"); new でインスタンス作成不可
  const teacherOne = Teacher.getInstance();
  const teacherSecond = Teacher.getInstance();
  console.log(teacherOne === teacherSecond); // true
  ```

## Interface

`interface` は，`type`と似たようなものだが，`type`は型定義をオブジェクトに対しても行えるのに対して，`interface`は**オブジェクトのみ**に対応している．

```ts
interface Human {
  name: string;
  age: number;
  greeting(message: string): void;
}

const human: Human = {
  name: "Tom",
  age: 10,
  greeting(message: string): void {
    console.log(message);
  },
};
```

- `implements`

  `interface`を使ってオブジェクトを事前に定義し，それを`implements`でクラスに対して適用することができる．

  注意点として，`constructor`で定義しているフィールドは，`interface`で定義されているものに限っては`public`または`readonly`のみ適用可能．  
  `private`，`protected`はエラーが発生する．

  また，`interface`の代わりに`type`で定義しても，`implements`することが可能(ただし，オブジェクトを定義した場合のみ)

  ```ts
  interface Human {
    name: string;
    age: number;
    greeting(message: string): void;
  }

  class Developer implements Human {
    constructor(public name: string, public age: number) {}

    greeting(message: string): void {
      console.log(message);
    }
  }
  ```

- `readonly`

  `interface`で定義したフィールドに対して`readonly`をつけていて，それを`implements`したクラスでのフィールドは`readonly`には**ならない**．

  あくまで`interface`は設計図であり，強制的に定義されたフィールドをクラスで用意する必要はあるものの，`readonly`属性は影響しない．

  そのため，下記のようにクラスの型で定義した変数にインスタンスを代入すると，その動作はクラスの型で定義されたものに準ずるものになり，`interface`の型で定義した変数にインスタンスを代入すると，またもその動作は`interface`で定義されたものに準ずるものになる．

  ```ts
  interface Human {
    readonly name: string;
    printName(this: Human): void;
  }

  class Developer implements Human {
    constructor(public name: string) {}

    printName(this: Developer): void {
      console.log(this.name);
    }
  }

  const developer: Developer = new Developer("Tom");
  developer.printName(); // Tom
  developer.name = "Bob"; // Developerクラスではpublicとなっており，変更可能
  developer.printName(); // Bob

  const human: Human = new Developer("Lisa");
  human.printName(); // Lisa
  human.name = "Olive"; // Humanインターフェイスはreadonlyとなっており，setできない コンパイルエラーが発生
  ```

- `extends`

  `interface`を`extends`して，定義したフィールドを継承することができる．

  ```ts
  interface Age {
    age: number;
  }

  interface Human extends Age {
    name: string;
  }

  class Developer implements Human {
    constructor(public name: string, public age: number) {}
  }
  ```

  継承先に同じ名前のフィールドがあったときは，似た型であれば上書き可能だが，違う型のときはコンパイルエラーが発生する．

  ```ts
  interface Age {
    age: string;
  }

  interface Age2 extends Age {
    // age: number; stringにnumberは代入不可能
    age: string; // 同じ型のためエラーにはならない
    age: "xyz"; // stringにリテラル型は代入可能のためエラーにはならない
  }
  ```

- `interface`で関数を定義

  本来は`type`で関数を定義するものだが，`interface`でも関数を定義することができる．

  ```ts
  // type add = (num1: number, num2: number) => number; typeで関数を定義
  // interfaceで関数を定義
  interface add {
    (num1: number, num2: number): number;
  }

  let addFunc: add;
  addFunc = (x: number, y: number) => {
    return x + y;
  };
  ```

- `?`(オプショナルパラメータ)

  変数名，関数名，引数名の直後に`?`をつけることで，**なくてもいい**という状態を作る．

  ```ts
  interface Human {
    name: string;
    age?: number;
  }

  class Designer implements Human {
    constructor(public name: string) {} // ageはなくてもいい
  }
  ```

## Advanced

- `&`

  二つのオブジェクトで定義されているフィールドを合体させる．

  ```ts
  type Engineer = {
    name: string;
    role: string;
  };

  type Blogger = {
    name: string;
    follower: number;
  };

  type EngineerBlogger = Engineer & Blogger;

  // Engineer，Bloggerで定義されている全てのフィールドを用意しなくてはならない
  const engineerBlogger: EngineerBlogger = {
    name: "Tom",
    role: "back-end",
    follower: 100000,
  };
  ```

  以下のようにまたは条件を`&`で記述すると，どちらにも存在する number が評価される

  ```ts
  type NumberBoolean = number | boolean;
  type StringNumber = string | number;

  // (number | boolean) & (string | number)
  // -> number
  type Mix = NumberBoolean & StringNumber;
  ```

- タイプガード

  型を確認することで，安全にアクセスできるようにする．

  ```ts
  function toUpperCase(x: string | number) {
    if (typeof x === "string") {
      // 変数xはstring型であると保障されたので，#toUpperCaseに安全にアクセスできる
      return x.toUpperCase();
    }
    return "";
  }
  ```

  オブジェクトのフィールドがあるかを確認することで，安全にアクセスできるようにする．

  ```ts
  type Engineer = {
    name: string;
    role: string;
  };

  type Blogger = {
    name: string;
  };

  type EngineerBlogger = Engineer | Blogger;

  function getRole(engineerBlogger: EngineerBlogger) {
    if ("role" in engineerBlogger) {
      // 変数engineerBloggerにroleがあると保障されたので，roleに安全にアクセスできる
      return engineerBlogger.role;
    }

    return "";
  }
  ```

  インスタンスを確認することで，安全にアクセスできるようにする．

  ```ts
  class Dog {
    speak() {
      console.log("bow");
    }
  }

  class Bird {
    speak() {
      console.log("tweet");
    }

    fly() {
      console.log("flutter");
    }
  }

  type Pet = Dog | Bird;

  function doPetBehavior(pet: Pet) {
    pet.speak();
    if (pet instanceof Bird) {
      // 変数petはBirdインスタンスであることが保障されたので，#flyに安全にアクセスできる
      pet.fly();
    }
  }
  ```

- タグ付き Union

  フィールドにリテラル型のフィールドを置き，型の判別を分かりやすくする．

  ```ts
  class Dog {
    kind: "dog" = "dog";
  }

  class Bird {
    kind: "bird" = "bird";
  }

  type Pet = Dog | Bird;

  function havePet(pet: Pet) {
    switch (pet.kind) {
      case "bird":
      // do something
      case "dog":
      // do something
    }
  }
  ```

- 型アサーション

  型を強制的に上書きし，アクセスしやすくする．  
  ２通りの書き方がある．

  ```ts
  const input = <HTMLInputElement>document.getElementById("input");
  const input = document.getElementById("input") as HTMLInputElement;
  ```

- `!` (Non-null assertion operator)

  これは`null`ではないと明示的に表現させる．

  ```ts
  function getNullOrString(): string | null {
    return "string";
  }

  const a = getNullOrString()!;
  ```

- インデックスシグネチャ

  ```ts
  interface Designer {
    name: string;
    // これを追加することで，後からフィールドを追加することが可能になる
    // ただ，string型のみしか宣言することが出来なくなる(ここにあるnameも含め)
    // [index: 型] の型は，フィールドの型．stringのときは文字も数字も出来るが，
    // numberのときは数字しか許容しない．
    [index: string]: string;
  }

  const designer: Designer = {
    name: "Tom",
    role: "Manager", // ないフィールドを追加することが可能
  };

  designer.xxx = "xxx"; // 後から追加することも可能
  ```
