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
  <button v-on:click="isVisible">click me!</button>
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
