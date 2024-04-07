const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Array to store the books
let books = [];

// Array to store the users
let users = [];

// JSON schema for user data
const userSchema = {
  type: "object",
  properties: {
    name: { type: "string" },
    email: { type: "string", format: "email" },
    borrowedBooks: { type: "array", items: { type: "string" } },
  },
  required: ["name", "email"],
};

// Endpoint to add a new user
app.post("/users", (req, res) => {
  const user = req.body;
  // Validate the user data using the JSON schema
  const { error } = require("jsonschema").validate(user, userSchema);
  if (error) {
    return res.status(400).json({ error: error.details[0].message });
  }
  // Add the new user to the users array
  users.push(user);
  // Respond with the new user
  res.json(user);
});

// Endpoint to get all users
app.get("/users", (req, res) => {
  // Respond with the list of users
  res.json(users);
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
