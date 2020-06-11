require("./src/db/mongoose");
const User = require("./src/models/user");

// 5edf9d6fc702992720f10569

User.findByIdAndUpdate(
  "5edf9d6fc702992720f10569",
  {
    age: 0,
  },
  {
    new: true,
  }
)
  .then((user) => {
    console.log(user);
    return User.countDocuments({
      age: user.age,
    });
  })
  .then((totalCount) => {
    console.log(totalCount);
  })
  .catch((e) => {
    console.log(e);
  });
