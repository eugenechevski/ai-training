function quantumSuperposition(qubit) {
  // Initialize an array to represent the quantum state of the qubit
  let state = [1, 0];

  // Apply the Hadamard gate to the qubit
  let hadamardGate = [
    [1 / Math.sqrt(2), 1 / Math.sqrt(2)],
    [1 / Math.sqrt(2), -1 / Math.sqrt(2)],
  ];

  state = state.map((x) => hadamardGate[0][x] + hadamardGate[1][x]);

  // Normalize the state
  state = state.map(
    (x) => x / Math.sqrt(state.reduce((a, b) => a + b ** 2, 0))
  );

  return state;
}

// Example usage:

const qubit = [1, 0]; // Qubit in the state |0
console.log("Initial qubit state:", qubit);
