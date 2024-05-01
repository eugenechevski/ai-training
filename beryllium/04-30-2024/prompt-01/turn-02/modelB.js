function fetchProjectData() {
  // Replace 'YOUR_SERVER_URL' with the actual server URL providing the JSON data
  const serverUrl = "YOUR_SERVER_URL";

  // Use XMLHttpRequest to perform the AJAX request
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // Request successful, parse the JSON data
      const projectData = JSON.parse(xhr.responseText);
      // Update the dashboard with the received data
      updateDashboard(projectData);
    }
  };
  xhr.open("GET", serverUrl, true);
  xhr.send();
}

function updateDashboard(projectData) {
  // Get references to the necessary DOM elements
  const projectTitleElement = document.getElementById("projectTitle");
  const projectDescriptionElement =
    document.getElementById("projectDescription");
  const projectStatusElement = document.getElementById("projectStatus");
  const projectStartDateElement = document.getElementById("projectStartDate");
  const projectEndDateElement = document.getElementById("projectEndDate");
  const teamMembersElement = document.getElementById("teamMembers");
  const tasksElement = document.getElementById("tasks");

  // Clear any existing data in the dashboard elements
  projectTitleElement.textContent = "";
  projectDescriptionElement.textContent = "";
  projectStatusElement.textContent = "";
  projectStartDateElement.textContent = "";
  projectEndDateElement.textContent = "";
  teamMembersElement.innerHTML = "";
  tasksElement.innerHTML = "";

  // Extract project information from the data
  const project = projectData.projects[0];
  const teamMembers = project.teamMembers;
  const tasks = project.tasks;

  // Update project details in the dashboard
  projectTitleElement.textContent = project.projectTitle;
  projectDescriptionElement.textContent = project.projectDescription;
  projectStatusElement.textContent = project.status;
  projectStartDateElement.textContent = new Date(
    project.startDate
  ).toLocaleDateString();
  projectEndDateElement.textContent = new Date(
    project.endDate
  ).toLocaleDateString();

  // Update team members in the dashboard
  teamMembers.forEach(function (member) {
    const memberElement = document.createElement("div");
    memberElement.textContent = `${member.name} (${member.role})`;
    teamMembersElement.appendChild(memberElement);
  });

  // Update tasks in the dashboard
  tasks.forEach(function (task) {
    const taskElement = document.createElement("div");
    taskElement.textContent = `${task.taskTitle} - Assigned to: ${
      task.assignee.name
    }, Deadline: ${new Date(task.deadline).toLocaleDateString()}, Status: ${
      task.status
    }`;
    tasksElement.appendChild(taskElement);

    // Add task timelines if available
    if (task.timelines.length > 0) {
      const timelinesElement = document.createElement("ul");
      taskElement.appendChild(timelinesElement);
      task.timelines.forEach(function (timeline) {
        const timelineElement = document.createElement("li");
        timelineElement.textContent = `Planned: ${new Date(
          timeline.planned
        ).toLocaleTimeString()}, Actual: ${new Date(
          timeline.actual
        ).toLocaleTimeString()}`;
        timelinesElement.appendChild(timelineElement);
      });
    }
  });
}
