// script.js

let missions = [];
let nextLaunchTime = null;

const missionsContainer = document.getElementById("missions-container");
const filterContainer = document.getElementById("filter-container");
const countdownContainer = document.getElementById("countdown-container");
const addMissionBtn = document.getElementById("add-mission-btn");

// Add event listener to add mission button
addMissionBtn.addEventListener("click", () => {
  const missionName = prompt("Enter mission name:");
  const missionDescription = prompt("Enter mission description:");
  if (missionName && missionDescription) {
    addMission(missionName, missionDescription);
  }
});

// Function to add a new mission
function addMission(name, description) {
  const mission = {
    name,
    description,
    status: "pending",
  };
  missions.push(mission);
  renderMissions();
}

// Function to render all missions
function renderMissions() {
  missionsContainer.innerHTML = "";
  missions.forEach((mission, index) => {
    const missionHTML = `
            <div class="mission ${
              mission.status === "launched" ? "mission-launched" : ""
            } ${mission.status === "completed" ? "mission-completed" : ""}">
                <h2 class="mission-name">${mission.name}</h2>
                <p class="mission-description">${mission.description}</p>
                <p class="mission-status">${mission.status}</p>
                <button class="launch-btn" data-index="${index}">Launch</button>
                <button class="complete-btn" data-index="${index}">Complete</button>
                <button class="delete-btn" data-index="${index}">Delete</button>
            </div>
        `;
    missionsContainer.innerHTML += missionHTML;
  });
  updateCountdownTimer();
}

// Function to update the countdown timer
function updateCountdownTimer() {
  const nextLaunch = missions.find((mission) => mission.status === "pending");
  if (nextLaunch) {
    const currentTime = new Date().getTime();
    const launchTime = new Date(nextLaunch.launchDate).getTime();
    const timeDiff = launchTime - currentTime;
    const days = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
    const hours = Math.floor(
      (timeDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
    );
    const minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);
    countdownContainer.innerHTML = `Next Launch: ${days} days ${hours} hours ${minutes} minutes ${seconds} seconds`;
    setTimeout(updateCountdownTimer, 1000);
  } else {
    countdownContainer.innerHTML = "No upcoming launches";
  }
}

// Function to mark a mission as launched
function launchMission(index) {
  missions[index].status = "launched";
  renderMissions();
}

// Function to mark a mission as completed
function completeMission(index) {
  missions[index].status = "completed";
  renderMissions();
}

// Function to delete a mission
function deleteMission(index) {
  missions.splice(index, 1);
  renderMissions();
}

// Add event listeners to launch, complete, and delete buttons
missionsContainer.addEventListener("click", (event) => {
  if (event.target.classList.contains("launch-btn")) {
    launchMission(event.target.dataset.index);
  } else if (event.target.classList.contains("complete-btn")) {
    completeMission(event.target.dataset.index);
  } else if (event.target.classList.contains("delete-btn")) {
    deleteMission(event.target.dataset.index);
  }
});

// Add event listeners to filter buttons
filterContainer.addEventListener("click", (event) => {
  if (event.target.classList.contains("filter-btn")) {
    const filter = event.target.dataset.filter;
    filterMissions(filter);
  }
});

// Function to filter missions by status
function filterMissions(filter) {
  const filteredMissions = missions.filter((mission) => {
    if (filter === "all") {
      return true;
    } else if (filter === "launched") {
      return mission.status === "launched";
    } else if (filter === "completed") {
      return mission.status === "completed";
    }
  });
  missionsContainer.innerHTML = "";
  filteredMissions.forEach((mission, index) => {
    const missionHTML = `
            <div class="mission ${
              mission.status === "launched" ? "mission-launched" : ""
            } ${mission.status === "completed" ? "mission-completed" : ""}">
                <h2 class="mission-name">${mission.name}</h2>
                <p class="mission-description">${mission.description}</p>
                <p class="mission-status">${mission.status}</p>
                <button class="launch-btn" data-index="${index}">Launch</button>
                <button class="complete-btn" data-index="${index}">Complete</button>
                <button class="delete-btn" data-index="${index}">Delete</button>
            </div>
        `;
    missionsContainer.innerHTML += missionHTML;
  });
}
