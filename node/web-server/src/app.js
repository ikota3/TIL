const express = require("express");

const app = express();
app.get("", (req, res) => {
  res.send("<h1>Hello express</h1>");
});

app.get("/help", (req, res) => {
  res.send({ name: "Tom", age: 27 });
});

app.get("/about", (req, res) => {
  res.send("<h1>About page</h1>");
});

app.get("/weather", (req, res) => {
  res.send({ forecast: "It is Sunny", location: "Tokyo" });
});

app.listen(8080, () => {
  console.log("Listening on 8080.");
});
