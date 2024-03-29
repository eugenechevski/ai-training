// Get the elements
const inputField = document.getElementById('input-field');
const hashOutput = document.getElementById('hash-output');

// Listen for changes in the input field
inputField.addEventListener('keyup', () => {
  // Calculate the MD5 hash of the input field's value
  const hash = md5(inputField.value);

  // Update the div element with the hash
  hashOutput.innerHTML = `Hash: ${hash}`;
});