 // JavaScript code to handle the edit button click event and open the modal
 document.addEventListener('DOMContentLoaded', function() {
  const editButtons = document.querySelectorAll('.edit-button');
  editButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      const modal = new bootstrap.Modal(document.getElementById('editUserModal'));
      modal.show();
    });
  });
});