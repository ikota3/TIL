require("./src/db/mongoose");
const User = require("./src/models/user");
const Task = require("./src/models/task");

// User.findByIdAndUpdate(
//   "5edf9d6fc702992720f10569",
//   {
//     age: 0,
//   },
//   {
//     new: true,
//   }
// )
//   .then((user) => {
//     console.log(user);
//     return User.countDocuments({
//       age: user.age,
//     });
//   })
//   .then((totalCount) => {
//     console.log(totalCount);
//   })
//   .catch((e) => {
//     console.log(e);
//   });

// const updateAgeAndCount = async (id, age) => {
//   const user = await User.findByIdAndUpdate(id, { age });
//   const count = await User.countDocuments({ age });
//   return count;
// };

// updateAgeAndCount("5edf9d6fc702992720f10569", 2)
//   .then((count) => {
//     console.log(count);
//   })
//   .catch((e) => {
//     console.log(e);
//   });

// const deleteTaskAndCount = async (id) => {
//   await Task.findByIdAndDelete(id);
//   return await Task.countDocuments({ completed: false });
// };

// deleteTaskAndCount("5edf87dfeff4733d489c9967")
//   .then((count) => {
//     console.log(count);
//   })
//   .catch((e) => {
//     console.log(e);
//   });
