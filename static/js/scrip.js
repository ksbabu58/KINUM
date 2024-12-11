function openSubcategory(category) {
    const modal = document.getElementById('subcategory-modal');
    const modalTitle = document.getElementById('modal-category-title');
    const modalList = document.getElementById('modal-subcategory-list');

    console.log('Category:', category);
    console.log('Modal:', modal);
    console.log('Modal Title:', modalTitle);
    console.log('Modal List:', modalList);

    // Define subcategories with their respective links
    const subcategories = {
        electronics: [
            { name: 'Phones', link: 'phones.html' },
            { name: 'Laptops', link: 'laptops.html' },
            { name: 'Tablets', link: 'tablets.html' }
        ],
        vehicles: [
            { name: 'Cars', link: 'cars.html' },
            { name: 'Motorcycles', link: 'motorcycles.html' },
            { name: 'Bicycles', link: 'bicycles.html' }
        ],
        furniture: [
            { name: 'Chairs', link: 'chairs.html' },
            { name: 'Tables', link: 'tables.html' },
            { name: 'Couches', link: 'couches.html' }
        ],
        realestate: [
            { name: 'Houses', link: 'houses.html' },
            { name: 'Apartments', link: 'apartments.html' },
            { name: 'Land', link: 'land.html' }
        ]
    };

    // Set modal title and clear previous content
    modalTitle.textContent = category.charAt(0).toUpperCase() + category.slice(1);
    modalList.innerHTML = '';

    // Populate modal with subcategory links
    subcategories[category].forEach(subcategory => {
        const subcategoryDiv = document.createElement('div');
        subcategoryDiv.classList.add('subcategory');
        subcategoryDiv.innerHTML = `<a href="${subcategory.link}" class="subcategory-link">${subcategory.name}</a>`;
        modalList.appendChild(subcategoryDiv);
    });

    // Show modal
    modal.style.display = 'block';
}

function closeModal() {
    const modal = document.getElementById('subcategory-modal');
    modal.style.display = 'none';
}
