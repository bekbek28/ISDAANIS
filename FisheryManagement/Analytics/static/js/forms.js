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

