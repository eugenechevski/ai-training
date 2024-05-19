const recipeForm = document.getElementById('recipe-form');
const recipeList = document.getElementById('recipe-list');

recipeForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const recipeName = document.getElementById('recipe-name').value.trim();
    const ingredients = document.getElementById('ingredients').value.trim();
    const instructions = document.getElementById('instructions').value.trim();

    if (recipeName && ingredients && instructions) {
        const recipeCard = document.createElement('DIV');
        recipeCard.classList.add('recipe-card');
        recipeCard.innerHTML = `
            <h3 class="recipe-name">${recipeName}</h3>
            <p class="ingredients">${ingredients}</p>
            <p class="instructions">${instructions}</p>
        `;
        recipeList.appendChild(recipeCard);

        recipeCard.addEventListener('click', () => {
            recipeCard.classList.toggle('expanded');
        });

        recipeForm.reset();
    } else {
        alert('Please fill in all fields!');
    }
});