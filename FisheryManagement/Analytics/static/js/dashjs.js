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



fetch('/unloadhistory/')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // Chart.js code for the first bar chart (Fishtype)
    const ctx = document.getElementById('Fishtype').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.species, // Use the 'species' data from Django view
        datasets: [{
          label: 'Quantity',
          data: data.quantities, // Use the 'quantities' data from Django view
          borderColor: getRandomColors(data.species.length), // Use random colors for each species
          backgroundColor: getRandomColors(data.species.length),
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
        labels: data.vessel, // Use the 'vessel' data from Django view
        datasets: [{
          label: 'Quantity',
          data: data.quantities, // Use the 'quantities' data from Django view
          borderColor: getRandomColors(data.vessel.length), // Use random colors for each vessel
          backgroundColor: getRandomColors(data.vessel.length),
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
        labels: data.origin, // Use the 'origin' data from Django view
        datasets: [{
          label: 'Quantity',
          data: data.quantities, // Use the 'quantities' data from Django view
          borderColor: getRandomColors(data.origin.length), // Use random colors for each origin
          backgroundColor: getRandomColors(data.origin.length),
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

    // Chart.js code for the first line chart (DailyCatch)
    const ctx4 = document.getElementById('DailyCatch').getContext('2d');
    new Chart(ctx4, {
      type: 'line',
      data: {
        labels: data.labels, // Use the 'labels' data from Django view
        datasets: [{
          label: 'Quantity',
          data: data.quantities, // Use the 'quantities' data from Django view
          borderColor: 'rgba(0, 2, 161, 1)',
          backgroundColor: getRandomColors2(1),
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
        labels: data.labels, // Use the 'labels' data from Django view
        datasets: [{
          label: 'Quantity',
          data: data.quantities, // Use the 'quantities' data from Django view
          borderColor: 'rgba(0, 2, 161, 1)',
          backgroundColor: getRandomColors2(1),
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
        labels: data.labels, // Use the 'labels' data from Django view
        datasets: [{
          label: 'Quantity',
          data: data.quantities, // Use the 'quantities' data from Django view
          borderColor: 'rgba(0, 2, 161, 1)',
          backgroundColor: getRandomColors2(1),
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
