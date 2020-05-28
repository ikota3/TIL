const path = require("path");
const express = require("express");
const hbs = require("hbs");

const app = express();
// Static directory path
const staticDirectory = path.join(__dirname, "../public");
// Template directory path
const viewsPath = path.join(__dirname, "../templates/views");
// Partial directory path
const partialPath = path.join(__dirname, "../templates/partials");

// Setup static path
app.use(express.static(staticDirectory));
// Setup hbs engine
app.set("view engine", "hbs");
// Setup hbs partial path
hbs.registerPartials(partialPath);

// Setup template path
app.set("views", viewsPath);

/**
 * ROOT
 */
app.get("", (req, res) => {
  res.render("index", {
    title: "Weather App",
    name: "Tom",
  });
});

/**
 * ABOUT
 */
app.get("/about", (req, res) => {
  res.render("about", {
    title: "About Me",
    name: "Tom",
  });
});

/**
 * HELP
 */
app.get("/help", (req, res) => {
  res.render("help", {
    helpText: "Helpful message",
    title: "Help",
    name: "Tom",
  });
});

/**
 * WEATHER
 */
app.get("/weather", (req, res) => {
  res.send({ forecast: "It is Sunny", location: "Tokyo" });
});

/**
 * HELP/*
 */
app.get("/help/*", (req, res) => {
  res.render("404", {
    title: "404",
    name: "Tom",
    errorMessage: "Help article not found.",
  });
});

/**
 * 404
 */
app.get("*", (req, res) => {
  res.render("404", {
    title: "404",
    name: "Tome",
    errorMessage: "Page not found.",
  });
});

app.listen(8080, () => {
  console.log("Listening on 8080.");
});
