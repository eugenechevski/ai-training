// Initialize the missions array
let missions = [];

// Function to add a new mission
function addMission(event) {
  event.preventDefault();
  const missionName = document.getElementById("mission-name").value;
  const missionDescription = document.getElementById(
    "mission-description"
  ).value;
  const newMission = {
    name: missionName,
    description: missionDescription,
    status: "pending",
    launchDate: new Date(Date.now() + Math.random() * 10000000), // random launch date in the future
  };
  missions.push(newMission);
  renderMissions();
  document.getElementById("mission-name").value = "";
  document.getElementById("mission-description").value = "";
}

// Function to render the missions list
function renderMissions() {
  const missionsList = document.getElementById("missions-list");
  missionsList.innerHTML = "";
  missions.forEach((mission, index) => {
    const missionListItem = document.createElement("li");
    missionListItem.innerHTML = `
      <h2>${mission.name}</h2>
      <p>${mission.description}</p>
      <p>Status: ${mission.status}</p>
      <button onclick="launchMission(${index})">Launch</button>
      <button onclick="completeMission(${index})">Complete</button>
      <button onclick="deleteMission(${index})">Delete</button>
    `;
    missionsList.appendChild(missionListItem);
  });
}

// Function to launch a mission
function launchMission(index) {
  missions[index].status = "launched";
  renderMissions();
}

// Function to complete a mission
function completeMission(index) {
  missions[index].status = "completed";
  renderMissions();
}

// Function to delete a mission
function deleteMission(index) {
  missions.splice(index, 1);
  renderMissions();
}

// Function to filter missions by status
function filterMissions() {
  const filterValue = document.getElementById("filter").value;
  if (filterValue === "all") {
    renderMissions();
  } else {
    const filteredMissions = missions.filter(
      (mission) => mission.status === filterValue
    );
    const missionsList = document.getElementById("missions-list");
    missionsList.innerHTML = "";
    filteredMissions.forEach((mission, index) => {
      const missionListItem = document.createElement("li");
      missionListItem.innerHTML = `
        <h2>${mission.name}</h2>
        <p>${mission.description}</p>
        <p>Status: ${mission.status}</p>
        <button onclick="launchMission(${index})">Launch</button>
        <button onclick="completeMission(${index})">Complete</button>
        <button onclick="deleteMission(${index})">Delete</button>
      `;
      missionsList.appendChild(missionListItem);
    });
  }
}

// Function to display the countdown timer for the next mission launch
function displayNextLaunchCountdown() {
  const nextLaunchDate = missions.find(
    (mission) => mission.status === "pending"
  ).launchDate;
  const now = new Date();
  const timeDiff = nextLaunchDate - now;
  const days = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
  const hours = Math.floor(
    (timeDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
  );
  const minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);
  document.getElementById("next-launch-countdown").innerHTML = `
    Next Launch: ${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds
  `;
}

// Initialize the countdown timer
setInterval(displayNextLaunchCountdown, 1000);

// Render the initial missions list
renderMissions();
