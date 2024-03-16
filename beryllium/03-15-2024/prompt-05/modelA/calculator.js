function add() {
  const num1 = parseFloat(document.getElementById("num1").value);
  const num2 = parseFloat(document.getElementById("num2").value);
  const result = num1 + num2;
  displayResult(result);
}

function subtract() {
  const num1 = parseFloat(document.getElementById("num1").value);
  const num2 = parseFloat(document.getElementById("num2").value);
  const result = num1 - num2;
  displayResult(result);
}

function multiply() {
  const num1 = parseFloat(document.getElementById("num1").value);
  const num2 = parseFloat(document.getElementById("num2").value);
  const result = num1 * num2;
  displayResult(result);
}

function divide() {
  const num1 = parseFloat(document.getElementById("num1").value);
  const num2 = parseFloat(document.getElementById("num2").value);

  if (num2 === 0) {
    alert("Cannot divide by zero!");
    return;
  }

  const result = num1 / num2;
  displayResult(result);
}

function clear() {
  document.getElementById("num1").value = "";
  document.getElementById("num2").value = "";
  document.getElementById("result").innerHTML = "0";
}

function displayResult(result) {
  document.getElementById("result").innerHTML = result;
}
