/* DARK MODE JAVASCRIPT CODE */
const body = document.querySelector("body"),
  modeToggle = body.querySelector(".mode-toggle");
sidebar = body.querySelector("nav");
sidebarToggle = body.querySelector(".sidebar-toggle");

let getMode = localStorage.getItem("mode");
if (getMode && getMode === "dark") {
  body.classList.toggle("dark");
}

let getStatus = localStorage.getItem("status");
if (getStatus && getStatus === "close") {
  sidebar.classList.toggle("close");
}

modeToggle.addEventListener("click", () => {
  body.classList.toggle("dark");
  if (body.classList.contains("dark")) {
    localStorage.setItem("mode", "dark");
  } else {
    localStorage.setItem("mode", "light");
  }
});

sidebarToggle.addEventListener("click", () => {
  sidebar.classList.toggle("close");
  if (sidebar.classList.contains("close")) {
    localStorage.setItem("status", "close");
  } else {
    localStorage.setItem("status", "open");
  }
});

function openLogoutModal() {
  document.getElementById('logoutModal').style.display = 'block';
}

function closeLogoutModal() { 
  document.getElementById('logoutModal').style.display = 'none';
}

function logout() {
  // Add your logout logic here
  // Retrieve the logout URL from the data attribute
  var logoutUrl = document.querySelector('[data-logout-url]').dataset.logoutUrl;
  // Redirect to the logout URL
  window.location.href = logoutUrl;
  // Close the modal after redirect (optional)
  closeLogoutModal();
}

// Function to get random colors for the bar chart
function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

document.addEventListener('DOMContentLoaded', function () {
  const placeOfCatchSelect = document.getElementById('placeofcatch');
  const monthSelect = document.getElementById('months');
  const yearSelect = document.getElementById('year');
  const ctx1 = document.getElementById('Fishtype').getContext('2d');
  const ctx4 = document.getElementById('DailyCatch').getContext('2d');
  const ctx5 = document.getElementById('MonthlyCatch').getContext('2d');
  const ctx6 = document.getElementById('YearlyCatch').getContext('2d');

  let fishtypeChart;
  let dailyChart;
  let monthlyChart;

  // Fetch initial data when the page loads
  fetch('http://127.0.0.1:8000/analytics/unloadingDashData/')
      .then(response => response.json())
      .then(data => {
          // Chart.js code for the first bar chart (Fishtype)
          fishtypeChart = new Chart(ctx1, {
              type: 'bar',
              data: {
                  labels: data.species_data.map(item => item.species_name),
                  datasets: [{
                      label: 'Quantity',
                      data: data.species_data.map(item => item.total_quantity),
                      borderColor: getRandomColor(data.species_data.length),
                      backgroundColor: getRandomColor(data.species_data.length),
                      borderWidth: 1.5
                  }]
              },
              options: {
                  legend: {
                      display: true,
                  },
                  scales: {
                      y: {
                          beginAtZero: true
                      }
                  }
              }
          });

          // Chart.js code for the fourth line chart (DailyCatch)
          dailyChart = new Chart(ctx4, {
              type: 'line',
              data: {
                  labels: data.labels_daily,
                  datasets: [{
                      label: 'Quantity',
                      data: data.quantities,
                      borderColor: 'rgba(0, 2, 161, 1)',
                      backgroundColor: getRandomColor(1),
                      borderWidth: 2
                  }]
              },
              options: {
                  scales: {
                      y: {
                          beginAtZero: true
                      }
                  }
              }
          });

          // Chart.js code for the fifth line chart (MonthlyCatch)
          monthlyChart = new Chart(ctx5, {
              type: 'line',
              data: {
                  labels: data.labels_monthly,
                  datasets: [{
                      label: 'Quantity',
                      data: data.quantities_monthly,
                      borderColor: 'rgba(0, 2, 161, 1)',
                      backgroundColor: getRandomColor(1),
                      borderWidth: 2
                  }]
              },
              options: {
                  scales: {
                      y: {
                          beginAtZero: true
                      }
                  }
              }
          });

          // Chart.js code for the sixth line chart (YearlyCatch)
          yearlyChart = new Chart(ctx6, {
              type: 'line',
              data: {
                  labels: data.labels_yearly,
                  datasets: [{
                      label: 'Quantity',
                      data: data.quantities_yearly,
                      borderColor: 'rgba(0, 2, 161, 1)',
                      backgroundColor: getRandomColor(1),
                      borderWidth: 2
                  }]
              },
              options: {
                  scales: {
                      y: {
                          beginAtZero: true
                      }
                  }
              }
          });

          // Update charts based on selected place of catch, month, and year
          function updateCharts() {
              const selectedPlaceOfCatch = placeOfCatchSelect.value;
              const selectedMonth = monthSelect.value;
              const selectedYear = yearSelect.value;

              fetch(`http://127.0.0.1:8000/analytics/unloadingDashData/?origin=${selectedPlaceOfCatch}&month=${selectedMonth}&year=${selectedYear}`)
                  .then(response => response.json())
                  .then(filteredData => {
                      // Update the fishtype chart
                      fishtypeChart.data.labels = filteredData.species_data.map(item => item.species_name);
                      fishtypeChart.data.datasets[0].data = filteredData.species_data.map(item => item.total_quantity);
                      fishtypeChart.update();

                      // Update the daily chart
                      dailyChart.data.labels = filteredData.labels_daily;
                      dailyChart.data.datasets[0].data = filteredData.quantities;
                      dailyChart.update();

                      // Update the monthly chart
                      monthlyChart.data.labels = filteredData.labels_monthly;
                      monthlyChart.data.datasets[0].data = filteredData.quantities_monthly;
                      monthlyChart.update();
                  });
          }

          // Set up event listeners for place of catch, month, and year selection
          placeOfCatchSelect.addEventListener('change', updateCharts);
          monthSelect.addEventListener('change', updateCharts);
          yearSelect.addEventListener('change', updateCharts);
      })
      .catch(error => console.error('Error fetching initial data:', error));
});

// Function to get random colors
function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}




