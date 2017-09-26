<head>
    <title>Weather Map</title>
    <style>
       #tempmap {
        width: 500px;
        height: 400px;
      }
	  #humiditymap {
        width: 500px;
        height: 400px;
      }
	  #icemap {
        width: 500px;
        height: 400px;
      }
    </style>
  </head>
  <body>
    <table>
        <tr>
            <th>Temperature</th>
            <th>Humidity</th>
        </tr>
        <tr>
            <td><div id="tempmap"></div></td>
            <td><div id="humiditymap"></div></td>
        </tr>
        <tr>
            <td></td>
        </tr>
        <tr>
            <th>ICE Temperature</th>
        </tr>
		<tr>
			<td><div id="icemap"></div></td>
		</tr>
    </table>
    <script>
      function get_temp_icon(temperature) {
        if (temperature < 48)   
          color = "blue";
        else if (temperature < 53)   
          color = "green";
        else if (temperature < 55)   
          color = "white";
        else if (temperature < 57)   
          color = "yellow";
        else if (temperature < 59)   
          color = "orange";
        else
          color = "red";
        temperature = Math.round(temperature)
        if (temperature < 0) {
          temp = "";
        }
        else if (temperature > 99) {
          temp = "";
        }
        else {
          temp = temperature.toString();
        }
        return "static/images/marker_" + color + temp + ".png"
      }
	  function get_humidity_icon(humidity) {
        if (humidity < 43)   
          color = "blue";
        else if (humidity < 45)   
          color = "green";
        else if (humidity < 47)   
          color = "white";
        else if (humidity < 49)   
          color = "yellow";
        else if (humidity < 50)   
          color = "orange";
        else
          color = "red";
        humidity = Math.round(humidity)
        if (humidity < 0) {
          h = "";
        }
        else if (humidity > 99) {
          h = "";
        }
        else {
          h = humidity.toString();
        }
        return "static/images/marker_" + color + h + ".png"
      }
	  function get_ice_icon(icetemp) {
        if (icetemp < 16)   
          color = "blue";
        else if (icetemp < 19)   
          color = "green";
        else if (icetemp < 20)   
          color = "white";
        else if (icetemp < 21)   
          color = "yellow";
        else if (icetemp < 22)   
          color = "orange";
        else
          color = "red";
        icetemp = Math.round(icetemp)
        if (icetemp < 0) {
          i = "";
        }
        else if (icetemp > 99) {
          i = "";
        }
        else {
          i = icetemp.toString();
        }
        return "static/images/marker_" + color + i + ".png"
      }
      function initMap() {
        var mapDiv = document.getElementById('tempmap');
		var humidityMapDiv = document.getElementById('humiditymap');
		var iceMapDiv = document.getElementById('icemap');
        var tmap = new google.maps.Map(mapDiv, {
            center: {lat: 41.145715	, lng: -81.336041},
            zoom: 19,
            zoomControl: false,
            scaleControl: false,
            scrollwheel: false,
            disableDoubleClickZoom: true
        });
		var hmap = new google.maps.Map(humidityMapDiv, {
            center: {lat: 41.145715	, lng: -81.336041},
            zoom: 19,
            zoomControl: false,
            scaleControl: false,
            scrollwheel: false,
            disableDoubleClickZoom: true
        });
		var imap = new google.maps.Map(iceMapDiv, {
            center: {lat: 41.145715	, lng: -81.336041},
            zoom: 19,
            zoomControl: false,
            scaleControl: false,
            scrollwheel: false,
            disableDoubleClickZoom: true
        });
        %for item in data:
            var location = {lat: {{item['lat']}}, lng: {{item['lon']}}}
            var marker = new google.maps.Marker({
                position: location,
                map : tmap,
                icon : get_temp_icon({{item['temp']}}),
                title: "{{str(item['temp'])}}"
            });
        %end
		%for item in data:
            var location = {lat: {{item['lat']}}, lng: {{item['lon']}}}
            var marker = new google.maps.Marker({
                position: location,
                map : hmap,
                icon : get_humidity_icon({{item['humidity']}}),
                title: "{{str(item['humidity'])}}"
            });
        %end
		%for item in data:
            var location = {lat: {{item['lat']}}, lng: {{item['lon']}}}
            var marker = new google.maps.Marker({
                position: location,
                map : imap,
                icon : get_humidity_icon({{item['icetemp']}}),
                title: "{{str(item['icetemp'])}}"
            });
        %end
      }
    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBtbdK74FKDvGpiwLQ56MY3JY9pDU3RqqQ&callback=initMap">
    </script>
  </body>