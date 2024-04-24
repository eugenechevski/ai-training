// Function to fetch traffic data from the server
async function fetchTrafficData() {
  try {
    const response = await fetch("http://your-server-url/traffic-data");
    // Check if the response is valid
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    // Handle any errors that occurred during the fetch
    console.error("Fetch error:", error);
    throw error;
  }
}
function updateDashboard(data) {
  // Update the dashboard UI with the received data
  // Implement your dashboard update logic here
  console.log("Updated dashboard with new data:", data);
}
function displayErrorMessage(error) {
  // Update the dashboard or display an error message to the user
  const errorElement = document.getElementById("error-message");
  errorElement.textContent = `Error: ${error.message}`;
  errorElement.style.display = "block";
}

function hideErrorMessage() {
  const errorElement = document.getElementById("error-message");
  errorElement.style.display = "none";
}
// Function to fetch data regularly and update the dashboard
async function runDashboard() {
  try {
    hideErrorMessage();
    const data = await fetchTrafficData();
    updateDashboard(data);
  } catch (error) {
    displayErrorMessage(error);
  }
  const delay = 15000; // 15 seconds
  setTimeout(runDashboard, delay);
}
// Start the dashboard updates
runDashboard();
