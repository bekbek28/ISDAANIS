document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("search-input");
    const tableRows = document.querySelectorAll(".table tbody tr");
    const searchBtn = document.getElementById("search-btn");
  
    function filterTable() {
      const searchQuery = searchInput.value.trim().toLowerCase();
  
      tableRows.forEach(function(row) {
        const rowData = row.textContent.trim().toLowerCase();
        if (rowData.includes(searchQuery)) {
          row.style.display = ""; // Show the row
        } else {
          row.style.display = "none"; // Hide the row
        }
      });
    }
  
    // Trigger search on button click
    searchBtn.addEventListener("click", function() {
      filterTable();
    });
  
    // Trigger search on keyup event in the search input
    searchInput.addEventListener("keyup", function() {
      filterTable();
    });
  });

  // JavaScript for the modal
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

  