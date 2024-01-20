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

function showLogoutSuccessMessage() {
  var logoutSuccessMessage = document.getElementById('logoutSuccessMessage');
  logoutSuccessMessage.style.display = 'block';

  // Hide the message after a certain duration (e.g., 3 seconds)
  setTimeout(function () {
    logoutSuccessMessage.style.display = 'none';
  }, 3000);
}

function logout() {
  // Add your logout logic here
  // For example, redirecting to the logout URL
  var logoutUrl = document.querySelector('[data-logout-url]').dataset.logoutUrl;
  window.location.href = logoutUrl;

  // Display logout success message
  showLogoutSuccessMessage();
}





/* to get random colors for the bar chart */
function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}





document.addEventListener('DOMContentLoaded', function () {
  const fishtypeSelect = document.getElementById('fishtypeOptions');
  const monthSelect = document.getElementById('months');
  const yearSelect = document.getElementById('year');
  const ctx2 = document.getElementById('Vessel').getContext('2d');
  const ctx3 = document.getElementById('PlaceOfCatch').getContext('2d');
  const ctx5 = document.getElementById('MonthlyCatch').getContext('2d');
  const ctx6 = document.getElementById('YearlyCatch').getContext('2d');

  let vesselChart;
  let placeOfCatchChart;
  let monthlyChart;
  let yearlyChart;

  function getRandomColor(length) {
    const letters = '0123456789ABCDEF';
    let colors = [];
    for (let i = 0; i < length; i++) {
      let color = '#';
      for (let j = 0; j < 6; j++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      colors.push(color);
    }
    return colors;
  }

  fetch('http://127.0.0.1:8000/analytics/unloadingDashData/')
    .then(response => response.json())
    .then(data => {
      // Chart.js code for the first bar chart (Vessels)
      vesselChart = new Chart(ctx2, {
        type: 'bar',
        data: {
          labels: data.vessel_data.map(item => item.vessel_name),
          datasets: [{
            label: 'Quantity',
            data: data.vessel_data.map(item => item.total_quantity),
            borderColor: getRandomColor(data.vessel_data.length),
            backgroundColor: getRandomColor(data.vessel_data.length),
            borderWidth: 1.5
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

      // Chart.js code for the second bar chart (PlaceOfCatch)
      placeOfCatchChart = new Chart(ctx3, {
        type: 'bar',
        data: {
          labels: data.origin_data.map(item => item.origin),
          datasets: [{
            label: 'Quantity',
            data: data.origin_data.map(item => item.total_quantity),
            borderColor: getRandomColor(data.origin_data.length),
            backgroundColor: getRandomColor(data.origin_data.length),
            borderWidth: 1.5
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

      // Chart.js code for the second line chart (MonthlyCatch)
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

      // Chart.js code for the third line chart (YearlyCatch)
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

      // Update charts based on selected fish type, month, and year
      function updateCharts() {
        const selectedFishType = fishtypeSelect.value;
        const selectedMonth = monthSelect.value;
        const selectedYear = yearSelect.value;

        fetch(`http://127.0.0.1:8000/analytics/unloadingDashData/?fish_type=${selectedFishType}&month=${selectedMonth}&year=${selectedYear}`)
          .then(response => response.json())
          .then(filteredData => {
            // Update the first chart (Vessels)
            vesselChart.data.labels = filteredData.vessel_data.map(item => item.vessel_name);
            vesselChart.data.datasets[0].data = filteredData.vessel_data.map(item => item.total_quantity);
            vesselChart.update();

            // Update the second chart (PlaceOfCatch)
            placeOfCatchChart.data.labels = filteredData.origin_data.map(item => item.origin);
            placeOfCatchChart.data.datasets[0].data = filteredData.origin_data.map(item => item.total_quantity);
            placeOfCatchChart.update();

            // Update the third chart (MonthlyCatch)
            monthlyChart.data.labels = filteredData.labels_monthly;
            monthlyChart.data.datasets[0].data = filteredData.quantities_monthly;
            monthlyChart.update();

          })
          .catch(error => console.error('Error updating charts:', error));
      }

      // Set up event listeners for fish type, month, and year selection
      fishtypeSelect.addEventListener('change', updateCharts);
      monthSelect.addEventListener('change', updateCharts);
      yearSelect.addEventListener('change', updateCharts);
    })
    .catch(error => console.error('Error fetching initial data:', error));
});





// Fetch data for the first time to populate the charts
fetch('http://127.0.0.1:8000/analytics/unloadingDashData/')
  .then(response => response.json())
  .then(data => {
    console.log('Fetched Data:', data);
  })
  .catch(error => console.error('Error fetching data:', error));
