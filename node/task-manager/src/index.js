const express = require("express");
require("./db/mongoose");
const userRouter = require("./routers/user");
const taskRouter = require("./routers/task");

const app = express();

// Auth
// app.use((req, res, next) => {
//   if (req.method === "GET") {
//     res.send("GET requests are disabled");
//   }
//   next();
// });

app.use((req, res, next) => {
  res.status(503).send("Maintenance mode");
});

app.use(express.json());
app.use(userRouter);
app.use(taskRouter);

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Listening on ${port}`);
});
