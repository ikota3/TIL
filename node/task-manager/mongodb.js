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
});
