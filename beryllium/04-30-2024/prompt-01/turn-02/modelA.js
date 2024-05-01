// Function to fetch project data and update the dashboard
async function fetchAndUpdateDashboard() {
  try {
    const projectData = {
        
    }
    // Assuming 'projectData' is an array of project objects following the provided schema
    const dashboardContainer = document.getElementById("dashboard");
    dashboardContainer.innerHTML = ""; // Clear the existing content

    // Function to render a single project and its tasks on the dashboard
    function renderProject(project) {
      const projectDiv = document.createElement("div");
      projectDiv.classList.add("project");
      // Set project details
      projectDiv.innerHTML = `
    <h2>${project.projectTitle}</h2>
    <p>${project.projectDescription}</p>
    <div class="project-status">Status: ${project.status}</div>
    <h3>Tasks:</h3>
    `;
      // Render tasks for the project
      const taskList = document.createElement("ul");
      project.tasks.forEach((task) => {
        const taskItem = document.createElement("li");
        taskItem.innerHTML = `
          <h4>${task.taskTitle}</h4>
          <p>Assigned to: ${task.assignee.name}</p>
          <p>Status: ${task.status}</p>
          <div class="task-timeline">
              <span>Planned: ${new Date(
                task.deadline
              ).toLocaleDateString()}</span>
              ${
                task.timelines.length > 0
                  ? `<span>Actual: ${new Date(
                      task.timelines[0].actual
                    ).toLocaleDateString()}</span>`
                  : ""
              }
          </div>
   `;
        taskList.appendChild(taskItem);
      });
      projectDiv.appendChild(taskList);
      dashboardContainer.appendChild(projectDiv);
    }
    // Loop through the projects and render each project on the dashboard
    projectData.forEach((project) => {
      renderProject(project);
    });
  } catch (error) {
    console.error("Error fetching data:", error);
    const errorMessage = document.createElement("h2");
    errorMessage.textContent = "Error fetching data. Please try again later.";
    dashboardContainer.appendChild(errorMessage);
  }
}
// Call the function to fetch and update the dashboard
fetchAndUpdateDashboard();
