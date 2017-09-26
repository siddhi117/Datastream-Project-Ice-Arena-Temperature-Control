<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var weather_data = google.visualization.arrayToDataTable([
          ['Time', 'Temperature', 'Humidity', 'Light'],
          %for row in rows:
            [ {{row['time']}}, {{row['temp']}}, {{row['humidity']}}, {{row['light']}} ],
          %end
        ]);
        
        var options1 = {
          title: 'Weather',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var ice_arena_data = google.visualization.arrayToDataTable([
          ['Time', 'Temperature', 'IceTemperature', 'Humidity', 'Light'],
          %for field in fields:
            [ {{field['time']}}, {{field['temp']}}, {{field['icetemp']}}, {{field['humidity']}}, {{field['light']}} ],
          %end
        ]);

        var options2 = {
          title: 'Ice Arena Weather',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('weather_chart'));
        chart.draw(weather_data, options1);
        var chart = new google.visualization.LineChart(document.getElementById('ice_arena_chart'));
        chart.draw(ice_arena_data, options2);
      }
    </script>
  </head>
  <body>
    <table>
        <tr>
          <td><div id="weather_chart" style="width: 500px; height: 400px"></div></td>
          <td><div id="ice_arena_chart" style="width: 500px; height: 400px"></div></td>
        </tr>
    </table>
  </body>
</html>