const stars = document.querySelectorAll('.star');
const display = document.getElementById('rating');

let currentRating = 0;

// Handle Clicking
stars.forEach(star => {
  star.addEventListener('click', () => {
    currentRating = star.getAttribute('data-value');
    updateStars(currentRating);
    display.value = `${currentRating}`;
  });
});

// Update visual state
function updateStars(rating) {
  stars.forEach(s => {
    s.classList.toggle('active', s.getAttribute('data-value') <= rating);
  });
}

// Load saved rating on startup
window.onload = () => {
  const saved = localStorage.getItem('userRating');
  if (saved) {
    currentRating = saved;
    updateStars(saved);
    display.innerText = `Rating: ${saved}`;
  }
};

