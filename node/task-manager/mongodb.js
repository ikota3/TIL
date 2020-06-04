// const mongodb = require("mongodb");
// const MongoClient = mongodb.MongoClient;
// const ObjectID = mongodb.ObjectID;

const { MongoClient, ObjectID } = require("mongodb");

const connURL = "mongodb://127.0.0.1:27017";
const dbName = "task-manager";

MongoClient.connect(connURL, { useUnifiedTopology: true }, (error, client) => {
  if (error) {
    return console.log("Unable to connect to database.");
  }

  console.log("Connected correctly.");
  const db = client.db(dbName);

  // db.collection("users").findOne(
  //   {
  //     _id: ObjectID("5ed8fe5c42675f43e47a15d3"),
  //   },
  //   (error, user) => {
  //     if (error) {
  //       return console.log("Unable to fetch from user.");
  //     }

  //     console.log(user);
  //   }
  // );

  db.collection("users")
    .find({
      age: 27,
    })
    .toArray((error, users) => {
      console.log(users);
    });

  db.collection("users")
    .find({
      age: 27,
    })
    .count((error, users) => {
      console.log(users);
    });
});
