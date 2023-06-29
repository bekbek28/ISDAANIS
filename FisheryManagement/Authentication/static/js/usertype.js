
  // Retrieve the logout message from the URL parameters
  const urlParams = new URLSearchParams(window.location.search);
  const message = urlParams.get('message');

  // Display the logout message
  const logoutMessage = document.getElementById('logout-message');
  logoutMessage.textContent = message;

