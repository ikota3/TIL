const fs = require("fs");
const chalk = require("chalk");

const filename = "notes.json";

/**
 * Saving content to notes
 *
 * @param {array} notes
 */
const saveNotes = (notes) => {
  const dataJSON = JSON.stringify(notes);
  fs.writeFileSync(filename, dataJSON);
};

/**
 * Loading content from notes
 * @returns array
 */
const loadNotes = () => {
  try {
    const dataBuffer = fs.readFileSync(filename);
    const dataJSON = dataBuffer.toString();
    return JSON.parse(dataJSON);
  } catch (e) {
    return [];
  }
};

/**
 * Add Handler
 * @param {string} title
 * @param {string} body
 */
const addNote = (title, body) => {
  const notes = loadNotes();
  const duplicateNote = notes.find((note) => {
    return note.title === title;
  });

  if (!duplicateNote) {
    notes.push({
      title: title,
      body: body,
    });
    saveNotes(notes);
    console.log(chalk.green.inverse(`Save ${title}.`));
  } else {
    console.log(chalk.red.inverse(`${title} already exists.`));
  }
};

/**
 * Remove Handler
 * @param {string} title
 */
const removeNote = (title) => {
  const notes = loadNotes();
  const filteredNotes = notes.filter((note) => {
    return note.title !== title;
  });

  if (notes.length !== filteredNotes.length) {
    saveNotes(filteredNotes);
    console.log(chalk.green.inverse(`Remove ${title}.`));
  } else {
    console.log(chalk.red.inverse(`${title} doesn't exists.`));
  }
};

/**
 * List Handler
 */
const listNotes = () => {
  loadNotes().forEach((note) => {
    console.log(chalk.blue.inverse(note.title));
  });
};

/**
 * Read Handler
 * @param {string} title
 */
const readNote = (title) => {
  note = loadNotes().find((note) => {
    return note.title === title;
  });

  if (note) {
    console.log(chalk.cyan.italic.bold.underline(note.title));
    console.log(note.body);
  } else {
    console.log(chalk.red.inverse(`${title} doesn't exists.`));
  }
};

module.exports = {
  addNote,
  removeNote,
  listNotes,
  readNote,
};
