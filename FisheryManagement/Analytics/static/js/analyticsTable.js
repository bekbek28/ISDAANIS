

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
        borderColor: ['rgba(0, 255, 171, 0.8)', 
        'rgba(0, 255, 171, 0.8)',
        'rgba(0, 255, 171, 0.8)',
        'rgba(0, 255, 171, 0.8)',
        'rgba(0, 255, 171, 0.8)',
        'rgba(0, 255, 171, 0.8)'],
        backgroundColor: getRandomColors(6),
        borderWidth: 1
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

  const ctx2 = document.getElementById('Vessel').getContext('2d');

  new Chart(ctx2, {
     type: 'bar',
     data: {
       labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
       datasets: [{
         label: '# of Votes',
         data: [12, 19, 3, 5, 2, 3],
         borderColor: ['rgba(0, 255, 171, 0.8)', 
         'rgba(0, 255, 171, 0.8)',
         'rgba(0, 255, 171, 0.8)',
         'rgba(0, 255, 171, 0.8)',
         'rgba(0, 255, 171, 0.8)',
         'rgba(0, 255, 171, 0.8)'],
         backgroundColor: getRandomColors(6),
         borderWidth: 1
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

   const ctx3 = document.getElementById('Place of Catch').getContext('2d');

   new Chart(ctx3, {
      type: 'bar',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
          label: '# of Votes',
          data: [12, 19, 3, 5, 2, 3],
          borderColor: ['rgba(0, 255, 171, 0.8)', 
          'rgba(0, 255, 171, 0.8)',
          'rgba(0, 255, 171, 0.8)',
          'rgba(0, 255, 171, 0.8)',
          'rgba(0, 255, 171, 0.8)',
          'rgba(0, 255, 171, 0.8)'],
          backgroundColor: getRandomColors(6),
          borderWidth: 1
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

    const ctx4 = document.getElementById('Daily Catch').getContext('2d');

   new Chart(ctx4, {
      type: 'bar',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
          label: '# of Votes',
          data: [12, 19, 3, 5, 2, 3],
          borderColor: ['rgba(0, 255, 171, 0.8)', 
          'rgba(0, 255, 171, 0.8)',
          'rgba(0, 255, 171, 0.8)',
          'rgba(0, 255, 171, 0.8)',
          'rgba(0, 255, 171, 0.8)',
          'rgba(0, 255, 171, 0.8)'],
          backgroundColor: getRandomColors(6),
          borderWidth: 1
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