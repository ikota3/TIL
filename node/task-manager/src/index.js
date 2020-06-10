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

app.get("/users", (req, res) => {
  User.find({})
    .then((users) => {
      res.status(200).send(users);
    })
    .catch((e) => {
      res.status(500).send();
    });
});

app.get("/users/:id", (req, res) => {
  const id = req.params.id;
  User.findById(id)
    .then((user) => {
      if (!user) {
        return res.status(404).send();
      }
      res.status(200).send(user);
    })
    .catch((e) => {
      res.status(500).send();
    });
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

app.get("/tasks", (req, res) => {
  Task.find({})
    .then((tasks) => {
      res.status(200).send(tasks);
    })
    .catch((e) => {
      res.status(500).send();
    });
});

app.get("/tasks/:id", (req, res) => {
  const id = req.params.id;
  Task.findById(id)
    .then((task) => {
      if (!task) {
        return res.status(404).send();
      }
      res.status(200).send(task);
    })
    .catch((e) => {
      res.status(500).send();
    });
});

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Listening on ${port}`);
});
