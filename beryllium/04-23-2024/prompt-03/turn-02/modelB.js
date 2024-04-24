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
  console.error("Error:", error);
}

function hideErrorMessage() {
  const errorElement = document.getElementById("error-message");
  errorElement.style.display = "none";
}
// Function to fetch data periodically and update the dashboard
function fetchDataAndUpdateDashboard() {
  hideErrorMessage(); // Hide any existing error messages
  fetchTrafficData().then(updateDashboard).catch(displayErrorMessage);
  setTimeout(fetchDataAndUpdateDashboard, 15000); // Fetch data every 15 seconds
}
// Call the function to start the periodic data fetch
fetchDataAndUpdateDashboard();
