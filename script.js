// Recipe data
const recipes = {
    france: {
        entrees: [
            {
                id: 'foie-gras',
                name: 'Foie Gras Terrine',
                image: 'https://source.unsplash.com/800x600/?foie-gras',
                time: '2h30',
                ingredients: [
                    '500g fresh foie gras',
                    'Salt and pepper',
                    '2 tbsp cognac',
                    '2 tbsp sugar',
                    '1 pinch nutmeg'
                ],
                instructions: [
                    'Clean the foie gras by removing the veins.',
                    'Season with salt, pepper, cognac, and sugar.',
                    'Marinate for 24 hours in the refrigerator.',
                    'Preheat oven to 100°C.',
                    'Place the foie gras in a terrine and bake for 2 hours.',
                    'Let cool and refrigerate for 48 hours before serving.'
                ]
            }
        ],
        plats: [
            {
                id: 'coq-au-vin',
                name: 'Coq au Vin',
                image: 'https://source.unsplash.com/800x600/?coq-au-vin',
                time: '3h',
                ingredients: [
                    '1 rooster (2kg)',
                    '1 bottle red wine',
                    '200g bacon',
                    '250g mushrooms',
                    '2 carrots',
                    '2 onions',
                    '2 garlic cloves',
                    'Bouquet garni',
                    'Salt and pepper'
                ],
                instructions: [
                    'Cut the rooster into pieces.',
                    'Marinate the pieces in red wine with vegetables and bouquet garni for 24 hours.',
                    'Brown the bacon and rooster pieces.',
                    'Add the marinade and simmer for 2h30.',
                    'Add mushrooms 30 minutes before the end.',
                    'Serve with steamed potatoes.'
                ]
            }
        ],
        desserts: [
            {
                id: 'tarte-tatin',
                name: 'Tarte Tatin',
                image: 'https://source.unsplash.com/800x600/?tarte-tatin',
                time: '1h30',
                ingredients: [
                    '1 shortcrust pastry',
                    '1kg apples',
                    '150g sugar',
                    '100g butter',
                    '1 pinch cinnamon'
                ],
                instructions: [
                    'Preheat oven to 180°C.',
                    'Caramelize sugar with butter.',
                    'Arrange peeled and quartered apples.',
                    'Cover with shortcrust pastry.',
                    'Bake for 45 minutes.',
                    'Flip the tart and serve warm.'
                ]
            }
        ]
    },
    japan: {
        entrees: [
            {
                id: 'miso-soup',
                name: 'Miso Soup',
                image: 'https://source.unsplash.com/800x600/?miso-soup',
                time: '20min',
                ingredients: [
                    '4 tbsp miso paste',
                    '1 liter water',
                    '200g tofu',
                    '2 green onions',
                    'Wakame seaweed',
                    '1 tbsp dashi'
                ],
                instructions: [
                    'Heat water with dashi.',
                    'Cut tofu into cubes and green onions into rounds.',
                    'Add tofu and seaweed.',
                    'Dilute miso paste in some broth.',
                    'Add miso paste and green onions.',
                    'Serve hot.'
                ]
            }
        ],
        plats: [
            {
                id: 'ramen',
                name: 'Ramen',
                image: 'https://source.unsplash.com/800x600/?ramen',
                time: '1h',
                ingredients: [
                    '400g ramen noodles',
                    '1 liter chicken broth',
                    '2 tbsp miso',
                    '200g pork',
                    '2 eggs',
                    'Green onions',
                    'Nori seaweed',
                    'Soy sauce'
                ],
                instructions: [
                    'Prepare broth with miso.',
                    'Cook noodles.',
                    'Marinate pork in soy sauce.',
                    'Cook soft-boiled eggs.',
                    'Assemble in bowls.',
                    'Garnish with green onions and seaweed.'
                ]
            }
        ],
        desserts: [
            {
                id: 'mochi',
                name: 'Mochi',
                image: 'https://source.unsplash.com/800x600/?mochi',
                time: '1h',
                ingredients: [
                    '200g glutinous rice',
                    '100g sugar',
                    'Cornstarch',
                    'Red bean paste'
                ],
                instructions: [
                    'Cook glutinous rice.',
                    'Pound rice until smooth paste.',
                    'Add sugar.',
                    'Form balls with the paste.',
                    'Fill with red bean paste.',
                    'Wrap in cornstarch.'
                ]
            }
        ]
    },
    italy: {
        entrees: [
            {
                id: 'bruschetta',
                name: 'Bruschetta',
                image: 'https://source.unsplash.com/800x600/?bruschetta',
                time: '15min',
                ingredients: [
                    '1 baguette',
                    '4 tomatoes',
                    '2 garlic cloves',
                    'Fresh basil',
                    'Olive oil',
                    'Salt and pepper'
                ],
                instructions: [
                    'Cut baguette into slices.',
                    'Toast the slices.',
                    'Rub with garlic.',
                    'Dice tomatoes.',
                    'Mix with basil and oil.',
                    'Top the bread slices.'
                ]
            }
        ],
        plats: [
            {
                id: 'pasta-carbonara',
                name: 'Pasta Carbonara',
                image: 'https://source.unsplash.com/800x600/?pasta-carbonara',
                time: '30min',
                ingredients: [
                    '400g spaghetti',
                    '200g pancetta',
                    '4 eggs',
                    '100g parmesan',
                    'Black pepper',
                    'Salt'
                ],
                instructions: [
                    'Cook pasta.',
                    'Cut pancetta into cubes.',
                    'Brown the pancetta.',
                    'Mix eggs with parmesan.',
                    'Mix pasta with pancetta.',
                    'Add egg-parmesan mixture off heat.'
                ]
            }
        ],
        desserts: [
            {
                id: 'tiramisu',
                name: 'Tiramisu',
                image: 'https://source.unsplash.com/800x600/?tiramisu',
                time: '30min + rest',
                ingredients: [
                    '250g mascarpone',
                    '3 eggs',
                    '100g sugar',
                    'Strong coffee',
                    'Ladyfinger cookies',
                    'Cocoa powder'
                ],
                instructions: [
                    'Separate whites from yolks.',
                    'Beat egg whites until stiff.',
                    'Mix yolks with sugar.',
                    'Incorporate mascarpone.',
                    'Dip cookies in coffee.',
                    'Alternate layers of cookies and cream.',
                    'Dust with cocoa.'
                ]
            }
        ]
    },
    thailand: {
        entrees: [
            {
                id: 'tom-yum',
                name: 'Tom Yum Soup',
                image: 'https://source.unsplash.com/800x600/?tom-yum-soup',
                time: '30min',
                ingredients: [
                    '1 liter chicken broth',
                    '200g shrimp',
                    '200g mushrooms',
                    '2 limes',
                    '2 chilies',
                    'Lemongrass',
                    'Kaffir lime leaves',
                    'Fish sauce'
                ],
                instructions: [
                    'Heat the broth.',
                    'Add lemongrass and kaffir lime leaves.',
                    'Add mushrooms.',
                    'Add shrimp.',
                    'Season with lime juice and fish sauce.',
                    'Garnish with chilies.'
                ]
            }
        ],
        plats: [
            {
                id: 'pad-thai',
                name: 'Pad Thai',
                image: 'https://source.unsplash.com/800x600/?pad-thai',
                time: '30min',
                ingredients: [
                    '200g rice noodles',
                    '200g shrimp',
                    '2 eggs',
                    '100g tofu',
                    'Bean sprouts',
                    'Peanuts',
                    'Tamarind sauce',
                    'Palm sugar'
                ],
                instructions: [
                    'Soak the noodles.',
                    'Stir-fry shrimp and tofu.',
                    'Add eggs.',
                    'Add noodles and sauce.',
                    'Mix with bean sprouts.',
                    'Garnish with peanuts.'
                ]
            }
        ],
        desserts: [
            {
                id: 'mango-sticky-rice',
                name: 'Mango Sticky Rice',
                image: 'https://source.unsplash.com/800x600/?mango-sticky-rice',
                time: '1h',
                ingredients: [
                    '200g sticky rice',
                    '2 ripe mangoes',
                    '200ml coconut milk',
                    '100g sugar',
                    'Salt'
                ],
                instructions: [
                    'Soak rice for 4 hours.',
                    'Steam the rice.',
                    'Heat coconut milk with sugar.',
                    'Pour over rice.',
                    'Serve with sliced mangoes.'
                ]
            }
        ]
    }
};

// Mobile navigation
const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-links');
const navLinks = document.querySelectorAll('.nav-links li');

burger.addEventListener('click', () => {
    nav.classList.toggle('nav-active');
    burger.classList.toggle('toggle');
});

// Country cards click event
document.querySelectorAll('.country-card').forEach(card => {
    card.addEventListener('click', () => {
        const country = card.getAttribute('data-country');
        console.log('Country clicked:', country); // Debug log
        displayCountryRecipes(country);
        document.querySelector('#recipes').scrollIntoView({ behavior: 'smooth' });
    });
});

// Display recipes for a country
function displayCountryRecipes(country) {
    console.log('Displaying recipes for:', country); // Debug log
    const recipeGrid = document.querySelector('.recipe-grid');
    recipeGrid.innerHTML = '';

    const countryRecipes = recipes[country];
    if (!countryRecipes) {
        console.log('No recipes found for:', country); // Debug log
        return;
    }

    // Get all recipes from all categories
    const allRecipes = [
        ...(countryRecipes.entrees || []),
        ...(countryRecipes.plats || []),
        ...(countryRecipes.desserts || [])
    ];

    console.log('Found recipes:', allRecipes.length); // Debug log

    // Display all recipes
    allRecipes.forEach(recipe => {
        const recipeCard = document.createElement('div');
        recipeCard.className = 'recipe-card';
        recipeCard.innerHTML = `
            <img src="${recipe.image}" alt="${recipe.name}">
            <div class="recipe-info">
                <h3>${recipe.name}</h3>
                <div class="time">
                    <i class="far fa-clock"></i>
                    ${recipe.time}
                </div>
            </div>
        `;

        recipeCard.addEventListener('click', () => {
            console.log('Recipe clicked:', recipe.name); // Debug log
            showRecipeDetails(recipe);
        });

        recipeGrid.appendChild(recipeCard);
    });
}

// Show recipe details
function showRecipeDetails(recipe) {
    console.log('Showing details for:', recipe.name); // Debug log
    
    const recipeDetails = document.getElementById('recipe-details');
    const recipeContent = document.getElementById('recipe-content');
    
    recipeContent.innerHTML = `
        <h2>${recipe.name}</h2>
        <img src="${recipe.image}" alt="${recipe.name}">
        <div class="recipe-info">
            <p><i class="far fa-clock"></i> Preparation time: ${recipe.time}</p>
            <h3>Ingredients</h3>
            <ul>
                ${recipe.ingredients.map(ingredient => `<li>${ingredient}</li>`).join('')}
            </ul>
            <h3>Instructions</h3>
            <ol>
                ${recipe.instructions.map(instruction => `<li>${instruction}</li>`).join('')}
            </ol>
        </div>
    `;

    recipeDetails.style.display = 'flex';

    // Close button event
    const closeBtn = recipeDetails.querySelector('.close-btn');
    closeBtn.addEventListener('click', () => {
        recipeDetails.style.display = 'none';
    });

    // Close when clicking outside
    recipeDetails.addEventListener('click', (e) => {
        if (e.target === recipeDetails) {
            recipeDetails.style.display = 'none';
        }
    });
}

// Animation au scroll
const sections = document.querySelectorAll('section');

const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

sections.forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'all 0.5s ease-out';
    observer.observe(section);
}); 