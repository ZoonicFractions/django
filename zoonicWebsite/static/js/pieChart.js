// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = "Poppins", "sans-serif";
Chart.defaults.global.defaultFontColor = '#858796';

// Function that generates the Pie Chart
async function generateChart(){
    // Attributes of the general dashboard
	var classroom = document.getElementById('classroom').innerHTML;
	var difficulty = document.getElementById('difficulty').innerHTML;

    // Calling the API
    const response = await fetch(`/api/level-participation-chart/${difficulty}/${classroom}`);
	const jsonData = await response.json();

    console.log(jsonData)

    // Generating the chart    
    if(jsonData.participation_list[0] == 0 && jsonData.participation_list[1] == 0 && jsonData.participation_list[2] == 0){
        document.getElementById(`myPieChart`).remove();
        document.getElementById(`div-chart`).remove();
    }else{
        document.getElementById(`info-paragraph`).remove();
    }

    var ctx = document.getElementById(`myPieChart`);
    var myPieChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: [
                'Nivel 1',
                'Nivel 2',
                'Nivel 3'
            ],
            datasets: [{
                data: [
                    jsonData.participation_list[0],
                    jsonData.participation_list[1],
                    jsonData.participation_list[2]
                ],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(54, 162, 235)',
                  'rgb(255, 205, 86)'
                ],
                hoverOffset: 4,
                label: 'My First Dataset',
            }]
        },
        options: {
            maintainAspectRatio: false,
        }
    });
}
generateChart()