function generateForm(jsonData) {
  // Create the form element
  const form = document.createElement("form");

  // Iterate through the JSON object
  for (const key in jsonData) {
    // Create a container for each field
    const fieldContainer = document.createElement("div");

    // Create the label
    const label = document.createElement("label");
    label.textContent = key;
    label.setAttribute("for", key);
    fieldContainer.appendChild(label);

    // Create the input field
    const input = document.createElement("input");
    input.setAttribute("type", "text");
    input.setAttribute("name", key);
    input.setAttribute("placeholder", jsonData[key]);
    input.setAttribute("id", key);
    fieldContainer.appendChild(input);

    // Add the field and its label to the form
    form.appendChild(fieldContainer);
  }

  // Return the generated form
  return form;
}

const myData = {
  firstName: "Enter your first name",
  lastName: "Enter your last name",
  email: "Enter your email",
};

const dynamicForm = generateForm(myData);
document.body.appendChild(dynamicForm);

