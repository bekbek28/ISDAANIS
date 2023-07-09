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
const getRandomColors = (count) => {
  const colors = [];
  const letters = '0123456789ABCDEF';
  for (let i = 0; i < count; i++) {
    let color = 'rgba(';
    for (let j = 0; j < 3; j++) {
      color += Math.floor(Math.random() * 256) + ', ';
    }
    color += '0.5)';
    colors.push(color);
  }
  return colors;
};


const ctx = document.getElementById('Fishtype').getContext('2d');
   
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      borderColor: ['rgba(0, 215, 255, 1)', 
                    'rgba(0, 215, 255, 1)',
                    'rgba(0, 215, 255, 1)',
                    'rgba(0, 215, 255, 1)',
                    'rgba(0, 215, 255, 1)',
                    'rgba(0, 215, 255, 1)'],
      backgroundColor: getRandomColors(6),
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


const ctx2 = document.getElementById('Vessel').getContext('2d');

new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [13, 19, 3, 5, 2, 3],
        borderColor: ['rgba(0, 215, 255, 1)', 
                      'rgba(0, 215, 255, 1)',
                      'rgba(0, 215, 255, 1)',
                      'rgba(0, 215, 255, 1)',
                      'rgba(0, 215, 255, 1)',
                      'rgba(0, 215, 255, 1)'],
        backgroundColor: getRandomColors(6),
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

  const ctx3 = document.getElementById('PlaceOfCatch').getContext('2d');
new Chart(ctx3, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderColor: ['rgba(0, 215, 255, 1)', 
                      'rgba(0, 215, 255, 1)',
                      'rgba(0, 215, 255, 1)',
                      'rgba(0, 215, 255, 1)',
                      'rgba(0, 215, 255, 1)',
                      'rgba(0, 215, 255, 1)'],
        backgroundColor: getRandomColors(6),
                          
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

 /* to get random colors in the line chart */
  const getRandomColors2 = (count) => {
    const colors = [];
    const letters = '0123456789ABCDEF';
    for (let i = 0; i < count; i++) {
      let color = 'rgba(';
      for (let j = 0; j < 3; j++) {
        color += Math.floor(Math.random() * 256) + ', ';
      }
      color += '5)';
      colors.push(color);
    }
    return colors;
  };
  
  const ctx4 = document.getElementById('DailyCatch').getContext('2d');
new Chart(ctx4, {
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderColor: ['rgba(0, 2, 161, 1)'],
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
  const ctx5 = document.getElementById('MonthlyCatch').getContext('2d');
new Chart(ctx5, {
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderColor: ['rgba(0, 2, 161, 1)'],
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

  const ctx6 = document.getElementById('YearlyCatch').getContext('2d');
new Chart(ctx6, {
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderColor: ['rgba(0, 2, 161, 1)', ],
      backgroundColor: getRandomColors2 (1),
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

