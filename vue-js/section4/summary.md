# Section4

### Vue インスタンスは複数作ることが出来、値を行き来させることが出来る

下記の通りに、複数インスタンスを作ることが出来る  
二つのインスタンスの値を行き来させることは可能だが、処理が煩雑になってしまうため、出来る限り一つにまとめたほうがいい  
それぞれが独立していて、別のインスタンスの値を動的に変えたい場合は使うのもいいかもしれない

```html
<div id="app1">
  <p>{{ message }}</p>
</div>

<div id="app2">
  <p>{{ message }}</p>
</div>

<script>
  const app1 = new Vue({
    el: "#app1",
    data: {
      message: "app1 instance",
    },
  });

  const app2 = new Vue({
    el: "#app2",
    data: {
      message: "app2 instance",
    },
  });

  // Change app1 message
  app1.message = "Changed app1 instance";
</script>
```

### Vuejs のリアクティブシステム

Vuejs では、最初に data プロパティに値をセットしていれば、`setter/getter` を用意し、あるイベント時に値が書き変わるような処理を書けば、そのイベントに応じて値が書き変わるが、後に値を加えた場合、`setter/getter` が用意されていないため、値が書き変わらない  
下記の例では、`message`は書き変わるが、`name`は書き変わらない

```html
<div id="app">
  <p>{{ message }}</p>
  <p>{{ name }}</p>
  <button @click="message = 'Change message'">Change message</button>
  <button @click="name = 'Change name'">Change name</button>
</div>

<script>
  const app = new Vue({
    el: "#app",
    data: {
      message: "Hello!",
    },
  });

  app.name = "Tarou";
</script>
```

### \$data を使うことで data プロパティにあるオブジェクトを参照できる

自インスタンスからだと、`this.$data`でアクセス出来る

```javascript
const app = new Vue({
  el: "#app",
  data: {
    message: "Hello!",
    name: "Tarou",
  },
  methods: {
    testFunc() {
      return this.$data; // {message: "Hello!", name: "Tarou"}
    },
  },
});

console.log(app.$data); // {message: "Hello!", name: "Tarou"}
```

### \$mount を使うことで、後から紐づける element を決める

`$mount("#app")`を使うことで、`el: "#app"` としていたものと同じ意味になる

```html
<div id="app">
  <p>{{ message }}</p>
</div>

<script>
  const app = new Vue({
    // el: "#app",
    data: {
      message: "Hello!",
    },
  });

  app.$mount("#app");
</script>
```

### template プロパティを使って HTML を描画する

`template`プロパティは、直に HTML を書くことで描画することが出来る

```html
<div id="app"></div>

<script>
  const app = new Vue({
    el: "#app",
    data: {
        message: "Hello!",
    }
    template: "<p>{{ message }}</p>";
  });
</script>
```

### render プロパティを使って HTML を描画する

`render`プロパティは、関数を定義し、引数のコールバック関数を用いて、<strong>仮想ノード</strong>の生成を行い、それを戻り値にする処理を行うことで描画することが出来る

```html
<div id="app"></div>

<script>
  const app = new Vue({
    el: "#app",
    data: {
        message: "Hello!",
    }
    render: function(createElement) {
        // Create p tag
        return createElement('p', this.message);
    }
  });
</script>
```

### 仮想 DOM

Vuejs では、実際に DOM に反映される前に、変更前と変更後の DOM を比べて、変更があった箇所のみを追加する処理を行っている  
実際の DOM を再作成すると、コストが非常にかかるため、実際は Javascript のオブジェクトである仮想 DOM で差分をとり、変更箇所を素早く見つけ、それのみを反映させるために、仮想 DOM が使われている
