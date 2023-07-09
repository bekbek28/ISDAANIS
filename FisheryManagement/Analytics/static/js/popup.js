$(document).ready(function() {
  $("#addUserBtn").click(function() {
    $("#addUserForm").css("display", "block");
  });

  $(".close-btn").click(function() {
    $("#addUserForm").css("display", "none");
  });
});
