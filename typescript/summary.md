# TypeScript

## Compile

```
tsc ${filename}
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
