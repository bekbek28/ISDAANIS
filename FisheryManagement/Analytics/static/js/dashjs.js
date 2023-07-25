/* DARK MODE JAVASCRIPT CODE */
const body = document.querySelector("body"),
      modeToggle = body.querySelector(".mode-toggle");
      sidebar = body.querySelector("nav");
      sidebarToggle = body.querySelector(".sidebar-toggle");

let getMode = localStorage.getItem("mode");
if(getMode && getMode ==="dark"){
    body.classList.toggle("dark");
}

let getStatus = localStorage.getItem("status");
if(getStatus && getStatus ==="close"){
    sidebar.classList.toggle("close");
}

modeToggle.addEventListener("click", () =>{
    body.classList.toggle("dark");
    if(body.classList.contains("dark")){
        localStorage.setItem("mode", "dark");
    }else{
        localStorage.setItem("mode", "light");
    }
});

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if(sidebar.classList.contains("close")){
        localStorage.setItem("status", "close");
    }else{
        localStorage.setItem("status", "open");
    }
})

function showLogoutMessage() {
  const logoutMessage = document.getElementById('logout-message');
  logoutMessage.textContent = 'You have been logged out.';
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
    // Chart.js code for the first bar chart (Fishtype)

    var ctx = document.getElementById('Fishtype').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: data.species_data.map(item => item.species_name), // Use the 'species' data from Django view
        datasets: [{
            label: 'Quantity',
            data: data.species_data.map(item => item.total_quantity), // Use the 'total_quantity' from the 'species_data'
            borderColor: getRandomColor(data.species.length), // Use random colors for each species
            backgroundColor: getRandomColor(data.species.length),
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


    // Chart.js code for the second bar chart (Vessel)
    const ctx2 = document.getElementById('Vessel').getContext('2d');
    new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: data.vessel_data.map(item => item.vessel_name), // Change 'vessels' to 'vessel'
            datasets: [{
                label: 'Quantity',
                data: data.vessel_data.map(item => item.total_quantity), // Use the 'total_quantity' from the 'vessel_data'
                borderColor: getRandomColor(data.vessel.length), // Use random colors for each vessel
                backgroundColor: getRandomColor(data.vessel.length),
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
    

    // Chart.js code for the third bar chart (PlaceOfCatch)
   const ctx3 = document.getElementById('PlaceOfCatch').getContext('2d');
new Chart(ctx3, {
    type: 'bar',
    data: {
        labels: data.origin_data.map(item => item.origin), // Change 'origins' to 'origin'
        datasets: [{
            label: 'Quantity',
            data: data.origin_data.map(item => item.total_quantity), // Use the 'total_quantity' from the 'origin_data'
            borderColor: getRandomColor(data.origin.length), // Use random colors for each origin
            backgroundColor: getRandomColor(data.origin.length),
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


    function getRandomColor() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }


    // Chart.js code for the first line chart (DailyCatch)
    const ctx4 = document.getElementById('DailyCatch').getContext('2d');
    new Chart(ctx4, {
      type: 'line',
      data: {
        labels: data.labels_daily,// Use the 'labels' data from Django view
        datasets: [{
          label: 'Quantity',
          data: data.quantities, // Use the 'quantities' data from Django view
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

    // Chart.js code for the second line chart (MonthlyCatch)
    const ctx5 = document.getElementById('MonthlyCatch').getContext('2d');
    new Chart(ctx5, {
      type: 'line',
      data: {
        labels: data.labels_monthly, // Use the 'labels' data from Django view
        datasets: [{
          label: 'Quantity',
          data: data.quantities_monthly, // Use the 'quantities' data from Django view
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
