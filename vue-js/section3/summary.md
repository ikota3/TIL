# Section3

### 条件に応じて描画させる

`v-if` を用いることで、条件によって描画させることが出来る  
以下の例では、 isOk が `true` であるから、 p タグにある OK! という文字列が表示される  
`v-else-if` を用いることで、 else if 条件を使うことが出来、 `v-else` を使うことで else 条件を使うことが出来る  
ただ、 `v-else-if` は `v-if` の直下  
`v-else` は `v-if` または `v-else-if` の直下に置かないとうまく機能しない

```html
<div id="app">
  <p v-if="isOk">OK!</p>
  <p v-else-if="maybeOk">Maybe OK!</p>
  <p v-else>Not OK!</p>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      isOk: true,
      maybeOk: false,
    },
  });
</script>
```

### まとめて条件で描画を制御したいときは template タグを利用してもいいかもしれない

`v-if` を一つ一つのタグに書くと非常に非効率であるし、可読性も下がってしまう  
そういったときにまとめて描画を制御したいときは、 `template` タグを使ってもいいかもしれない  
`template` タグはグルーピングで使用され、画面に描画されないため、煩雑なコードになるのを防げるかもしれない

```html
<div id="app">
  <template v-if="isVisible">
    <p>こんにちは</p>
    <p>わたしは</p>
    <p>FEW?GWE#?@5です</p>
  </template>
  <button v-on:click="isVisible = !isVisible">click me!</button>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      isVisible: true,
    },
  });
</script>
```

### 頻繁に何かを切り替える処理でパフォーマンスを高めたいときは v-show を使う

`v-show` は、初期描画の際は分岐に関わらず描画するため、コストはかかるが、頻繁に表示・非表示を繰り返したいときは、`v-if` と異なり、DOM に追加したり消したりをしていないため(`style="display: none;"` を要素に追加しているだけ) なので、そういう時に使うといい

```html
<div id="app">
  <p v-show="isVisible">v-show</p>
  <button v-on:click="isVisible = !isVisible">click me!</button>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      isVisible: true,
    },
  });
</script>
```

### 配列やオブジェクトを、 v-for を使って描画する

`v-for` を使うことで配列やオブジェクトを描画することができる  
オブジェクトの場合は順番が保証されないため、注意して使わなければならない  
また、`v-for="n in 10"` とすることで、1 から 10 までの数字を使うことが出来る

```html
<div id="app">
  <ul>
    <li v-for="fruit in fruits">
      {{ fruits }}
    </li>
  </ul>
  <!-- 添え字も取得 -->
  <ul>
    <li v-for="(fruit, index) in fruits">
      {{ index }}-{{ fruits }}
    </li>
  </ul>

  <ul>
    <li v-for="value in object">
      {{ value }}
    </li>
  </ul>
  <!-- キーも取得 -->
  <ul>
    <li v-for="(value, key) in object">
      {{ key }}: {{ value }}
    </li>
  </ul>
  <!-- 添え字も取得 -->
  <ul>
    <li v-for="(value, key, index) in object">
      {{ index }} {{ key }}: {{ value }}
    </li>
  </ul>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      fruits: ["Apple", "Banana", "Grape"],
      object: {
        firstName: "Tarou",
        lastName: "Tekitou",
        age: 20,
      },
    },
  });
</script>
```

### v-for を使って描画した要素を消す操作や追加したりするとバグになりやすいので、key 属性をつけるといい

`key` 属性に<strong>固有の値</strong>を付けることで、描画されたそれぞれの配列の要素と紐づくようになり、その配列の要素が操作されると、その操作に応じた描画を行うようにできる  
例えば、`Apple` の要素が削除される操作が行われれば、その時に描画された`input` タグも削除される

```html
<div id="app">
  <ul>
    <div v-for="fruit in fruits" v-bind:key="fruit">
      <p>{{ fruit }}</p>
      <input type="text" />
    </div>
  </ul>
</div>

<script>
  new Vue({
    el: "#app",
    data: {
      fruits: ["Apple", "Banana", "Grape"],
    },
  });
</script>
```
