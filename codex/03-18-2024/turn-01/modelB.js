document.body.appendChild(document.createElement("form"));
document.body.getElementsByTagName("form")[0].setAttribute("id", "dynamicForm");

function generateForm(formData, formId = "dynamicForm") {
  // Get the reference to the form element
  const form = document.getElementById(formId);
  if (!form) {
    console.error(`Form with ID "${formId}" not found.`);
    return;
  }

  // Clear any existing content
  form.innerHTML = "";

  // Iterate through the JSON object
  for (const key in formData) {
    const value = formData[key];

    // Create a label for the input
    const label = document.createElement("label");
    label.htmlFor = key;
    label.textContent = `${key}: `;
    form.appendChild(label);

    // Create the appropriate input element based on the value type
    let inputElement;
    if (typeof value === "boolean") {
      inputElement = document.createElement("input");
      inputElement.type = "checkbox";
      inputElement.checked = value; // Set initial state for checkboxes
    } else if (Array.isArray(value)) {
      // Handle arrays as multi-select
      inputElement = document.createElement("select");
      inputElement.multiple = true;
      value.forEach((optionValue) => {
        const option = document.createElement("option");
        option.value = optionValue;
        option.text = optionValue;
        inputElement.appendChild(option);
      });
    } else {
      inputElement = document.createElement("input");
      inputElement.type = "text";
      inputElement.placeholder = value;
    }

    inputElement.name = key;
    inputElement.id = key;
    form.appendChild(inputElement);

    // Add a line break
    form.appendChild(document.createElement("br"));
  }
}

// Example usage:
const jsonObject = {
  name: "John Doe",
  email: "johndoe@example.com",
  subscribed: true,
  interests: ["coding", "music"],
};

generateForm(jsonObject);


