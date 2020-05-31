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
