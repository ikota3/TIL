# Section2

### 二重中括弧を使って描画する

Vue でデータを描画するには、まず Vue インスタンスを生成する必要がある  
下記で設定しているプロパティは以下である

- `el` (element) -> HTML 要素とを紐づかせる
- `data` -> 文字列や数値、オブジェクトなどを設定出来る(基本はプレーンな値を置く)
- `methods` -> メソッドを定義できる

`data` プロパティに属しているから data.message などで書けそうだが、Vue の仕様上、 message とだけ書くことで用いることが可能だ  
また、真偽地を使った三項演算子の活用や、関数の呼び出しも出来る  
ただし、`{{ const num = 0 }}` などの変数や関数の定義は出来ない。

```html
<div id="app">
  <p>{{ message }}</p>
  <p>{{ number + 5 }}</p>
  <p>{{ isActive ? 'activate' : 'nonactive' }}</p>
  <p>{{ sayHi() }}</p>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      message: "Hello World!",
      number: 0,
      isActive: true,
    },
    methods: {
      sayHi: function () {
        return "Hi!";
      },
    },
  });
</script>
```

### methods で定義した関数内で data で定義した変数を用いる

`data` プロパティで定義した変数にアクセスするには、`this` を用いることでアクセスすることができる

```javascript
new Vue({
  el: "#app",
  data: {
    num: 0,
  },
  methods: {
    dataNumber: function () {
      return this.num;
    },
  },
});
```

### 一度だけ描画する

以下の例では、message を sayHi 関数内で値を変更しているが、`v-once` を使うことによって、sayHi 関数内で書き変わった message は参照されずに、message で定義された初期値が参照されるようになる

```html
<div id="app">
  <p v-once>{{ message }}</p>
  <p>{{ sayHi() }}</p>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      message: "Hello World!",
    },
    methods: {
      sayHi: function () {
        this.message = "Change message";
        return this.message;
      },
    },
  });
</script>
```

### データを HTML として出力する

`data` プロパティに定義した変数を HTML として出力したいときは、 `v-html` を使うことで出力できる

```html
<div id="app">
  <div v-html="html"></div>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      html: "<h1>This is h1 tag.</h1>",
    },
  });
</script>
```

### タグの属性値をデータに紐づける

タグの属性で `data` にある変数を使いたいときは、単純に `href="{{ url }}"`としても、url 先が`{{ url }}`という文字列になってしまい、変数が展開されていない状態となってしまう  
そのため、タグの属性でも変数を展開するようにするためには、 `v-bind:属性="{{ someVariable }}"` とする必要がある  
また、 `:属性` と省略する記法もある

```html
<div id="app">
  <a v-bind:href="url">Google</a>
  <a :href="url">Google</a>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      url: "https://google.com",
    },
  });
</script>
```

### タグの属性をデータに紐づける

タグの属性を `data` にある変数から使いたいときは、`[]`を使うことで出来る

```html
<div id="app">
  <a :[attribute]="url">Google</a>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      attribute: "href",
      url: "https://google.com",
    },
  });
</script>
```

### タグの属性をオブジェクトでまとめて書く

複数の属性をまとめて書く方法は、下記のようにすると出来る

```html
<div id="app">
  <a v-bind="googleObject">Google</a>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      googleObject: {
        href: "https://google.com",
        id: "0",
      },
    },
  });
</script>
```

### クリック時の DOM イベント発生時に特定の処理をさせる

ボタンのクリック時などの DOM イベント時に特定の処理をさせたいときは、 `v-on:DOMイベント名="someThingToExecute"`とすることで、イベント発生時に処理を走らせることができる  
`@DOMイベント名="someThingToExecute"` という省略した記法もある  
`someThingToExecute` の中には関数だけでなく、 `number++` でも機能する

```html
<div id="app">
  <p>{{ number }} Clicks!</p>
  <button v-on:click="countUp"></button>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      number: 0,
    },
    methods: {
      countUp: function () {
        this.number++;
      },
    },
  });
</script>
```

### v-on 使用時のイベント情報を取得する

以下の例では、Some text にマウスのカーソルがあったときに、その時の X 軸と Y 軸を表示するものである  
`$event` を引数に渡し、定義した関数の引数を追加することで、イベント情報を受け取ることが出来る  
以下では一つしか引数がないので、呼び出し側が `changeMousePosition` とすることでも出来る

```html
<div id="app">
  <p v-on:mousemove="changeMousePosition($event)">Some text</p>
  <p>X: {{ x }}, Y: {{ y }}</p>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      x: 0,
      y: 0,
    },
    methods: {
      changeMousePosition: function (event) {
        this.x = event.clientX;
        this.y = event.clientY;
      },
    },
  });
</script>
```

### 頻繁に使われる処理を簡略化したイベント修飾子を使う

本来なら、event 情報を受け取り `disableMouseMovement` や、 `disableLink` のような関数で出来るが、より簡略化した記法がある  
以下の例だと、stopPropagation を .stop 、 preventDefault を .prevent とすることで同じ動作をさせることが出来る  
また、処理を繋げることもでき、 .stop.prevent のようにすることもできる

```html
<div id="app">
  <p v-on:mousemove.stop="changeMousePosition">Disable the mousemove event</p>
  <p>X: {{ x }}, Y: {{ y }}</p>
  <a v-on:click.prevent href="https://google.com">Google</a>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      x: 0,
      y: 0,
    },
    methods: {
      changeMousePosition: function (event) {
        this.x = event.clientX;
        this.y = event.clientY;
      },
      disableMouseMovement: function (event) {
        event.stopPropagation();
      },
      disableLink: function (event) {
        event.preventDefault();
      },
    },
  });
</script>
```

### キーボード押下時にイベントを発生させる

キーボード押下時のイベントを検出するときは、`v-on:keyup.キー名`で出来る  
以下の例では、エンターキー押下時にアラートを出す処理が行われる
また、例によって、 keyup.enter.space と繋げることもできる  
上記だと、エンタキーとスペースキー押下時に処理が行われる

```html
<div id="app">
  <input type="text" v-on:keyup.enter="myAlert" />
</div>

<script>
  new Vue({
    el: "#app",
    methods: {
      myAlert: function () {
        alert("Enter key event triggered!");
      },
    },
  });
</script>
```

### 双方向バインディング

以下の例では、`input` タグの初期値が `data` にある message から取得され、`input`の中身を編集すると、`p` タグにある message も書き変わるという内容である

```html
<div id="app">
  <input type="text" v-model="message" />
  <p>{{ message }}</p>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      message: "Hello!",
    },
  });
</script>
```

### computed プロパティを使って動的なデータを表示する

関数みたく `()` はつけるとエラーになるので、 `()` はつけないようにする  
`methods` と似たようなプロパティであり、 `methods` でも再現は出来るが、 `computed` は `methods` と違い、関数内の依存関係を見て、必要に応じて実行しているため、動的なデータを表示する際は `computed` を使ったほうがいい  
逆に `methods` は、関係のない画面の描画が起きるたびに実行される

```html
<div id="app">
  <p>{{ counter }}</p>
  <button @click="counter++">Plus 1</button>
  <p>{{ lessThanThree }}</p>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      counter: 0,
    },
    computed: {
      lessThanThree: function () {
        return this.counter > 3 ? "3より大きい" : "3以下";
      },
    },
  });
</script>
```

### ウォッチャを使って、データが変わったときに特定の処理をする

非同期処理を行う際に、 `watch` が使われる  
データの変更を監視させて、何かしら条件に一致したときに処理をしたいときとかに使える

```html
<div id="app">
  <p>{{ counter }}</p>
  <button @click="counter++">Plus 1</button>
  <p>{{ lessThanThree }}</p>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      counter: 0,
    },
    computed: {
      lessThanThree: function () {
        return this.counter > 3 ? "3より大きい" : "3以下";
      },
    },
    watch: {
      counter: function () {
        var vm = this;
        setTimeout(function () {
          vm.counter = 0;
        }, 3000);
      },
    },
  });
</script>
```

### 複数のオブジェクトを配列構文で適用する

オブジェクトを複数バインディングしたいときは、配列構文を用いることで、適用可能

```html
<div id="app">
  <h1 :style="[baseStyle, h1Style]">Hello!</h1>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      baseStyle: {
        fontSize: "60px",
      },
      h1Style: {
        color: "red",
        "background-color": "blue",
      },
    },
  });
</script>
```

## まとめ

- `el` は HTML のタグと紐づかせる
- `data` は 初期値などのデータを置ける
- `methods` は 関数を定義することが出来る
- `{{}}` を使うことで変数を展開することが出来る
- `data` プロパティに Vue インスタンス内でアクセスしたいときは、`this` を使う
- 一度だけ描画したいときは、`v-once` を使う
- HTML を そのまま表示したいときは、`v-html="someVariable"` で出来る
- タグの属性値に `data` を使いたいときは、`v-bind:属性="someVariable"` で出来る  
   タグの属性に `data` を使いたいときは、上にある属性のところを `[someVariable]`にすることで出来る  
   `v-bind` はまとめてオブジェクトで、複数の属性を設定することが出来る  
   複数のオブジェクトをまとめて適用したいときは、`[baseObject, spareObject]`とすることで適用できる  
   `:属性="someVariable"` という省略した記法もある
- `v-on` はイベント発生時に処理したいものがあったときに使える  
  `v-on:DOMイベント名="someThingToExecute"` で指定することが出来る  
  `@DOMイベント名="someThingToExecute"` という省略した記法もある  
  `v-on` 使用時のイベント情報は、 `$event` に入っている
- `v-model` を使うことで、双方向バインディングを作成できる
- 動的なデータを扱う際に `computed` プロパティを使うことで、 `methods` プロパティより効率的に関数が呼び出されるように出来る  
  `computed` プロパティは、依存関係にあるものが画面の描画に関係していたら実行されるため、無関係な描画の際は呼び出されることがない  
  `computed` プロパティを呼び出す際は、関数を呼び出すみたいに `()` はつけない
- `watch` プロパティを使うことで、データの変更を監視させて、何かしら条件に一致したときに処理をしたいときとかに使える
