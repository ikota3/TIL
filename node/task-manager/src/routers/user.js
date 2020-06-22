const express = require("express");
const router = new express.Router();
const multer = require("multer");
const User = require("../models/user");
const auth = require("../middleware/auth");

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
 * UPLOAD AVATAR IMAGE
 */
const upload = multer({
  limits: {
    fileSize: 1000000,
  },
  fileFilter(req, file, cb) {
    if (!file.originalname.match(/\.(jpg|jpeg|png)$/)) {
      return cb(new Error("Please upload jpg, jpeg or png."));
    }
    cb(undefined, true);
  },
});
router.post(
  "/users/me/avatar",
  auth,
  upload.single("upload"),
  async (req, res) => {
    req.user.avatar = req.file.buffer;
    try {
      await req.user.save();
      res.status(200).send();
    } catch (e) {
      res.status(500).send();
    }
  },
  (error, req, res, next) => {
    res.status(400).send({ error: error.message });
  }
);

/**
 * DELETE AVATAR IMAGE
 */
router.delete("/users/me/avatar", auth, async (req, res) => {
  try {
    req.user.avatar = undefined;
    await req.user.save();
    res.status(200).send();
  } catch (e) {
    res.status(500).send(e);
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
 * UPDATE USER BY ID
 */
router.patch("/users/me", auth, async (req, res) => {
  const updateKeys = Object.keys(req.body);
  const allowedKeys = ["name", "email", "password", "age"];
  const isValid = updateKeys.every((updateKey) => {
    return allowedKeys.includes(updateKey);
  });
  if (!isValid) {
    return res.status(400).send({ error: "Invalid field." });
  }

  const user = req.user;
  updateKeys.forEach((updateKey) => {
    user[updateKey] = req.body[updateKey];
  });

  try {
    await user.save();
    res.status(200).send(user);
  } catch (e) {
    res.status(400).send(e);
  }
});

/**
 * DELETE USER BY ID
 */
router.delete("/users/me", auth, async (req, res) => {
  try {
    await req.user.remove();
    res.status(200).send(req.user);
  } catch (e) {
    res.status(500).send();
  }
});

module.exports = router;
