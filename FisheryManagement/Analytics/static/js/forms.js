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

function closeModals() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}

function submitForm() {
  // You can add your form submission logic here
  // For demonstration purposes, let's update a div with the success message
  var successMessageDiv = document.getElementById("successMessage");
  successMessageDiv.innerHTML = "Form submitted successfully!";
  successMessageDiv.style.display = "block";

  // After successful submission, close the modal
  closeModals();
}

function close() {
  // This function is called when the "Cancel" button is clicked
  // Add any additional logic here if needed
  closeModals();
}





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


/* // Function to toggle vessel options based on unload type
function toggleVesselOptions() {
  var unloadTypeSelect = document.getElementById('typeofUnloadOptions');
  var vesselInput = document.getElementById('vessel');
  var selectedValue = unloadTypeSelect.value;

  console.log("Selected unload type:", selectedValue); // Log selected unload type

  if (selectedValue.includes('Inland')) {
      console.log("Unload type is Inland");
      vesselInput.value = ''; // Clear vessel field
      vesselInput.disabled = true; // Disable vessel input
  } else {
      console.log("Unload type is not Inland");
      vesselInput.disabled = false; // Enable vessel input
  }
}

// Add event listener for change event on unload type select element
document.getElementById('typeofUnloadOptions').addEventListener('change', toggleVesselOptions);

// Call the function once on page load to ensure initial state is set correctly
toggleVesselOptions();




// Function to prevent typing in the vessel field when disabled
function preventTyping(event) {
  console.log("preventTyping function called");
  if (event.target.disabled) {
      console.log("Typing prevented in disabled vessel field");
      event.preventDefault();
  }
}

// Add event listeners
window.addEventListener('load', function() {
  console.log("Page loaded");
  toggleVesselOptions(); // Ensure vessel input is disabled on page load if necessary
  document.getElementById('typeofUnloadOptions').addEventListener('change', toggleVesselOptions);
  document.getElementById('vessel').addEventListener('keydown', preventTyping);
});
 */