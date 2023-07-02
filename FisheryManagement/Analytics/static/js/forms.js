/* Javascript code for making a dropdown function in navbars */
window.addEventListener('click', function(e) {
  var dropdowns = document.getElementsByClassName('dropdown-content');
  for (var i = 0; i < dropdowns.length; i++) {
    var openDropdown = dropdowns[i];
    if (!openDropdown.classList.contains('hidden') && !openDropdown.parentNode.contains(e.target)) {
      openDropdown.classList.add('hidden');
    }
  }
});

// Add this script to your JavaScript file

// Get the dark mode toggle checkbox element
const darkModeToggle = document.getElementById('darkModeToggle');

// Function to toggle dark mode
function toggleDarkMode() {
  const body = document.body;
  body.classList.toggle('dark-mode');
}

// Add event listener to the dark mode toggle checkbox
darkModeToggle.addEventListener('change', toggleDarkMode);
