const express = require("express");
require("./db/mongoose");
const User = require("./models/user");
const Task = require("./models/task");

const app = express();
app.use(express.json());

app.post("/users", (req, res) => {
  if (req.body) {
    const user = new User(req.body);
    user
      .save()
      .then(() => {
        res.status(201).send(user);
      })
      .catch((e) => {
        res.status(400).send(e);
      });
  }
});

app.post("/tasks", (req, res) => {
  if (req.body) {
    const task = new Task(req.body);
    task
      .save()
      .then(() => {
        res.status(201).send(task);
      })
      .catch((e) => {
        res.status(400).send(e);
      });
  }
});

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Listening on ${port}`);
});
