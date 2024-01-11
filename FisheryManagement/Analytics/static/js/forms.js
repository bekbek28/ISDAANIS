/* Javascript code for making a dropdown function in different inputs */
window.addEventListener('click', function(e) {
  var dropdowns = document.getElementsByClassName('dropdown-content');
  for (var i = 0; i < dropdowns.length; i++) {
    var openDropdown = dropdowns[i];
    if (!openDropdown.classList.contains('hidden') && !openDropdown.parentNode.contains(e.target)) {
      openDropdown.classList.add('hidden');
    }
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const dateField = document.getElementById('dateofCatch');
  datepicker(dateField);
});

document.getElementById('dateofCatch').valueAsDate = new Date();




function openModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "block";
}

function closeModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}

function confirmSubmit() {
  // Implement form submission logic here
  alert("Form submitted successfully!");
  closeModal();
  updateSubmitButton(); // Change the submit button text or style after submission
}

function updateSubmitButton() {
  var submitButton = document.getElementById("submitButton");
  submitButton.innerText = "Submitted"; // Change the text to "Submitted" or customize as needed
  submitButton.disabled = true; // Optionally disable the button after submission
}

// Close the modal if the user clicks outside of it
window.onclick = function (event) {
  var modal = document.getElementById("myModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

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
