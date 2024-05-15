// Get the modal element
const modal = document.querySelector('.modal');

// Get the modal content elements
const modalTitle = document.querySelector('.modal-title');
const modalDescription = document.querySelector('.modal-description');

// Get the close button
const closeButton = document.querySelector('.close');

// Add event listeners to each project
document.querySelectorAll('.project').forEach((project) => {
    project.addEventListener('click', () => {
        // Get the project info
        const projectName = project.querySelector('h3').textContent;
        const projectDescription = project.querySelector('p').textContent;

        // Set the modal content
        modalTitle.textContent = projectName;
        modalDescription.textContent = projectDescription;

        // Show the modal
        modal.style.display = 'block';
    });
});

// Add an event listener to the close button
closeButton.addEventListener('click', () => {
    // Hide the modal
    modal.style.display = 'none';
});