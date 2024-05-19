const recipeForm = document.getElementById("recipe-form");
const recipeList = document.getElementById("recipe-list");

if (recipeName && ingredients && instructions) {
    const recipeCard = document.createElement('LI');
    recipeCard.classList.add('recipe-card');
    recipeCard.innerHTML = `
        <h3 class="recipe-name">${recipeName}</h3>
        <div class="recipe-details">
            <p class="recipe-ingredients">Ingredients: ${ingredients}</p>
            <p class="recipe-instructions">Instructions: ${instructions}</p>
        </div>
    `;
    recipeList.appendChild(recipeCard);

    recipeCard.addEventListener('click', () => {
        const recipeDetails = recipeCard.querySelector('.recipe-details');
        recipeDetails.classList.toggle('show');
    });
}
