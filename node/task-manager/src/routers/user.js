const express = require("express");
const User = require("../models/user");
const auth = require("../middleware/auth");
const router = new express.Router();

/**
 * LOGIN
 */
router.post("/users/login", async (req, res) => {
  try {
    const user = await User.findByCredentials(
      req.body.email,
      req.body.password
    );
    const token = await user.generateAuthToken();
    await res.send({ user, token });
  } catch (e) {
    res.status(401).send();
  }
});

/**
 * LOGOUT
 */
router.post("/users/logout", auth, async (req, res) => {
  try {
    req.user.tokens = req.user.tokens.filter((token) => {
      return token.token !== req.token;
    });
    await req.user.save();

    res.status(200).send();
  } catch (e) {
    res.status(500).send();
  }
});

/**
 * LOGOUT ALL
 */
router.post("/users/logoutAll", auth, async (req, res) => {
  try {
    req.user.tokens = [];
    await req.user.save();

    res.status(200).send();
  } catch (e) {
    res.status(500).send();
  }
});

/**
 * CREATE USER
 */
router.post("/users", async (req, res) => {
  if (req.body) {
    const user = new User(req.body);

    try {
      await user.save();
      const token = await user.generateAuthToken();
      res.status(201).send({ user, token });
    } catch (e) {
      res.status(400).send(e);
    }
  }
});

/**
 * GET AUTHENTICATED USER
 */
router.get("/users/me", auth, async (req, res) => {
  res.send(req.user);
});

/**
 * GET USER BY ID
 */
router.get("/users/:id", async (req, res) => {
  const id = req.params.id;
  try {
    const user = await User.findById(id);
    if (!user) {
      return res.status(404).send();
    }
    res.status(200).send(user);
  } catch (e) {
    res.status(500).send();
  }
});

/**
 * UPDATE USER BY ID
 */
router.patch("/users/:id", async (req, res) => {
  const updateKeys = Object.keys(req.body);
  const allowedKeys = ["name", "email", "password", "age"];
  const isValid = updateKeys.every((updateKey) =>
    allowedKeys.includes(updateKey)
  );
  if (!isValid) {
    return res.status(400).send({ error: "Invalid updates!" });
  }

  try {
    const user = await User.findById(req.params.id);
    if (!user) {
      return res.status(404).send();
    }

    updateKeys.forEach((updateKey) => (user[updateKey] = req.body[updateKey]));
    await user.save();

    // XXX いる？
    if (!user) {
      return res.status(404).send();
    }
    res.status(200).send(user);
  } catch (e) {
    res.status(400).send(e);
  }
});

/**
 * DELETE USER BY ID
 */
router.delete("/users/:id", async (req, res) => {
  try {
    const user = await User.findByIdAndDelete(req.params.id);
    if (!user) {
      return res.status(404).send();
    }

    res.status(200).send(user);
  } catch (e) {
    res.status(500).send();
  }
});

module.exports = router;
