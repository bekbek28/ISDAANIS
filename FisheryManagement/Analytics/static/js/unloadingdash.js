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


fetch('http://127.0.0.1:8000/analytics/unloadingDashData/')
  .then(response => response.json())
  .then(data => {


  // Chart.js code for the first bar chart (Vessels)
const ctx2 = document.getElementById('Vessel').getContext('2d');
const vesselChart = new Chart(ctx2, {
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
const ctx3 = document.getElementById('PlaceOfCatch').getContext('2d');
const placeOfCatchChart = new Chart(ctx3, {
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


// Add an event listener to the fish type select element
const fishtypeSelect = document.getElementById('fishtypeOptions');
fishtypeSelect.addEventListener('change', function () {
    // Get the selected fish name
    const selectedFish = fishtypeSelect.value;
    console.log('Selected Fish:', selectedFish);

    // Filter data based on the selected fish
    const filteredVesselData = data.vessel_data.filter(item => item.species_name === selectedFish);
    const filteredOriginData = data.origin_data.filter(item => item.species_name === selectedFish);

    // Log filtered data
    console.log('Filtered Vessel Data:', filteredVesselData);
    console.log('Filtered Origin Data:', filteredOriginData);

    // Update the charts with the filtered data
    console.log('Updating Vessel Chart');
    vesselChart.data.labels = filteredVesselData.map(item => item.vessel_name);
    vesselChart.data.datasets[0].data = filteredVesselData.map(item => item.total_quantity);
    vesselChart.update();

    console.log('Updating PlaceOfCatch Chart');
    placeOfCatchChart.data.labels = filteredOriginData.map(item => item.origin);
    placeOfCatchChart.data.datasets[0].data = filteredOriginData.map(item => item.total_quantity);
    placeOfCatchChart.update();
});




    function getRandomColor() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }

    // Chart.js code for the second line chart (MonthlyCatch)
    const ctx5 = document.getElementById('MonthlyCatch').getContext('2d');
    new Chart(ctx5, {
      type: 'line',
      data: {
        labels: data.labels_monthly, // Use the 'labels' data from Django view
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
    const ctx6 = document.getElementById('YearlyCatch').getContext('2d');
    new Chart(ctx6, {
      type: 'line',
      data: {
        labels: data.labels_yearly, // Use the 'labels' data from Django view
        datasets: [{
          label: 'Quantity',
          data: data.quantities_yearly, // Use the 'quantities' data from Django view
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

  
    
  });
