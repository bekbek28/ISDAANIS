// JavaScript code to handle form submission and reset search input value when it's empty
const searchInput = document.getElementById('search-input');
const searchForm = document.getElementById('search-form');

searchForm.addEventListener('submit', function(event) {
    if (searchInput.value.trim() === '') {
        searchInput.removeAttribute('name'); // Remove the search query parameter from the form submission
    }
});

var modal = document.getElementById("logoutModal");

// Get the button that opens the modal
var btn = document.getElementById("logoutButton");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// Get the button that opens the modal
var btn = document.getElementById("logoutButton");

// Get the modal
var modal = document.getElementById("logoutModal");

// When the user clicks the button, open the modal 
btn.onclick = function() {
    // Get the data-logout-url attribute value
    var logoutUrl = btn.getAttribute("data-logout-url");

    // Open the modal
    modal.style.display = "block";
}

// Function to close the modal
function closeModal() {
    modal.style.display = "none";
}

// Function to perform logout (update as needed)
function performLogout() {
    // Add your logout logic here
    console.log("Performing logout");
    // For example, redirect to the logout URL
    var logoutUrl = btn.getAttribute("data-logout-url");
    if (logoutUrl) {
        window.location.href = logoutUrl;
    } else {
        console.error("Logout URL not found");
    }
}

// Close the modal if the user clicks outside of it
window.onclick = function(event) {
    if (event.target == modal) {
        closeModal();
    }
}

var userIdToDelete;

function showConfirmationModal(userId) {
    userIdToDelete = userId;
    document.getElementById('confirmationModal').style.display = 'block';
}

function hideConfirmationModal() {
    document.getElementById('confirmationModal').style.display = 'none';
}

function confirmDelete() {
    // Send the delete request with the user ID
    window.location.href = "{% url 'Analytics:delete_user' id=user.id %}".replace('user.id', userIdToDelete);
    hideConfirmationModal(); // Hide the modal after sending the request
}