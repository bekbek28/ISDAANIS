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



