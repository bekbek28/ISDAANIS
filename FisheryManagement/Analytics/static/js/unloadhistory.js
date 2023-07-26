// JavaScript code to handle form submission and reset search input value when it's empty
const searchInput = document.getElementById('search-input');
const searchForm = document.getElementById('search-form');

searchForm.addEventListener('submit', function(event) {
    if (searchInput.value.trim() === '') {
        searchInput.removeAttribute('name'); // Remove the search query parameter from the form submission
    }
});
