const mongoose = require("mongoose");

mongoose.connect("mongodb://127.0.0.1:27017/task-manager-api", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const User = mongoose.model("User", {
  name: {
    type: String,
    required: true,
  },
  age: {
    type: Number,
  },
});

const Tom = new User({
  name: "Tom",
});

Tom.save()
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.log(error);
  });

// const Task = mongoose.model("Task", {
//   description: String,
//   completed: Boolean,
// });

// const firstTask = new Task({
//   description: "This is my first task to finish.",
//   completed: false,
// });

// firstTask
//   .save()
//   .then((result) => {
//     console.log(result);
//   })
//   .catch((error) => {
//     console.log(error);
//   });
