document.addEventListener('DOMContentLoaded', function() {
    // Add animation to nutrition and recommendation sections when they appear
    const nutritionSection = document.querySelector('.nutrition');
    const recommendationsSection = document.querySelector('.recommendations');
    
    if (nutritionSection) {
        nutritionSection.style.opacity = '0';
        setTimeout(() => {
            nutritionSection.style.transition = 'opacity 0.5s ease';
            nutritionSection.style.opacity = '1';
        }, 300);
    }
    
    if (recommendationsSection) {
        recommendationsSection.style.opacity = '0';
        setTimeout(() => {
            recommendationsSection.style.transition = 'opacity 0.5s ease';
            recommendationsSection.style.opacity = '1';
        }, 600);
    }
    
    // Form validation
    const foodForm = document.querySelector('form');
    const foodInput = document.getElementById('food');
    
    if (foodForm) {
        foodForm.addEventListener('submit', function(e) {
            if (!foodInput.value.trim()) {
                e.preventDefault();
                foodInput.classList.add('error');
                setTimeout(() => {
                    foodInput.classList.remove('error');
                }, 1000);
            }
        });
    }
});