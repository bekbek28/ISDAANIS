// JavaScript code to handle form submission and reset search input value when it's empty
const searchInput = document.getElementById('search-input');
const searchForm = document.getElementById('search-form');

searchForm.addEventListener('submit', function(event) {
    if (searchInput.value.trim() === '') {
        searchInput.removeAttribute('name'); // Remove the search query parameter from the form submission
    }
});

function openModal() {
    document.getElementById("logoutModal").style.display = "block";
  }
  
  function closeModal() {
    document.getElementById("logoutModal").style.display = "none";
  }
  
  function cancelLogout() {
    closeModal();
    // Additional logic for canceling logout
  }
  
  // Update the logout link in the modal before opening it
  document.getElementById("logoutLink").addEventListener("click", function() {
    closeModal();
  });
