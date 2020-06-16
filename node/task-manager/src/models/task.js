const mongoose = require("mongoose");
const bcrypt = require("bcrypt");

const taskSchema = new mongoose.Schema({
  description: {
    type: String,
    required: true,
    trim: true,
  },
  completed: {
    type: Boolean,
    default: false,
  },
});

// taskSchema.pre("save", async function (next) {
//   const task = this;
//   if (task.isModified("password")) {
//     task.
//   }
// });

const Task = mongoose.model("Task", taskSchema);

module.exports = Task;
