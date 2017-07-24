 function updateTime(){
  var time = new Date ( );

  var currentHours = time.getHours ( );
  var currentMinutes = time.getMinutes ( );

  // Pad the minutes and seconds with leading zeros, if required
  currentMinutes = ( currentMinutes < 10 ? "0" : "" ) + currentMinutes;

  // Choose either "AM" or "PM" as appropriate
  var timeOfDay = ( currentHours < 12 ) ? "AM" : "PM";

  // Convert the hours component to 12-hour format if needed
  currentHours = ( currentHours > 12 ) ? currentHours - 12 : currentHours;

  // Convert an hours component of "0" to "12"
  currentHours = ( currentHours == 0 ) ? 12 : currentHours;

  // Compose the string for display
  var currentTimeString = currentHours + ":" + currentMinutes + ' ' + timeOfDay;

  // Update the time display
  document.getElementById("time").innerHTML = currentTimeString;

}

function updateDate() {
  var date = new Date ( );

  months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
  days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];

  document.getElementById("day").innerHTML = days[date.getDay()];
  document.getElementById("date").innerHTML = months[date.getMonth()] + ' ' + date.getDate() + ', ' + date.getFullYear();
}



function loadWeather() {
  currentWeatherDiv = document.getElementById("currentWeather");
  forecastDiv = document.getElementById("forecastArea");

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
       var currentInfo = JSON.parse(this.responseText);

       //Set variables for Current Weather
       var currentTemp = currentInfo[0][0].current_observation.temp_f;
       var currentIcon = currentInfo[0][0].current_observation.icon_url;
       var currentWeatherState = currentInfo[0][0].current_observation.weather;
       var currentLocation = currentInfo[0][0].current_observation.display_location.full;
       var todaysHighLow = '&uarr; ' + currentInfo[1].forecast.simpleforecast.forecastday[0].high.fahrenheit + '&#176; ' + ' | ' + ' &darr; ' + currentInfo[1].forecast.simpleforecast.forecastday[0].low.fahrenheit + '&#176; ';
       
       //Update Current Weather
       currentWeatherDiv.innerHTML = currentLocation;
       currentWeatherDiv.insertAdjacentHTML('beforeend', '<br />' + currentTemp + '&#176; ' + '<img src=\"' + currentIcon + '\" >' );
       currentWeatherDiv.insertAdjacentHTML('beforeend', '<br />' + currentWeatherState);
       currentWeatherDiv.insertAdjacentHTML('beforeend', '<br />' + todaysHighLow);
      
      //Set Variables for Forecast
      
      var tomorrowsWeather = [currentInfo[1].forecast.simpleforecast.forecastday[1].date.weekday, currentInfo[1].forecast.simpleforecast.forecastday[1].icon_url, currentInfo[1].forecast.simpleforecast.forecastday[1].high.fahrenheit, currentInfo[1].forecast.simpleforecast.forecastday[1].low.fahrenheit]
      var oneDayAfterWeather = [currentInfo[1].forecast.simpleforecast.forecastday[2].date.weekday, currentInfo[1].forecast.simpleforecast.forecastday[2].icon_url, currentInfo[1].forecast.simpleforecast.forecastday[2].high.fahrenheit, currentInfo[1].forecast.simpleforecast.forecastday[2].low.fahrenheit]
      var twoDayAfterWeather = [currentInfo[1].forecast.simpleforecast.forecastday[3].date.weekday, currentInfo[1].forecast.simpleforecast.forecastday[3].icon_url, currentInfo[1].forecast.simpleforecast.forecastday[3].high.fahrenheit, currentInfo[1].forecast.simpleforecast.forecastday[3].low.fahrenheit]

      console.log(currentInfo[1].forecast.simpleforecast)


      //Update Forecast 
      forecastDiv.innerHTML = tomorrowsWeather[0] + '  ' + '<img src=\"' + tomorrowsWeather[1] + '\" > ' + '&nbsp; &uarr; ' + tomorrowsWeather[2] + '&#176; ' + ' | ' + ' &darr; ' + tomorrowsWeather[3] + '&#176; ';
      forecastDiv.insertAdjacentHTML('beforeend', '<br />' + oneDayAfterWeather[0] + '  ' + '<img src=\"' + oneDayAfterWeather[1] + '\" > ' + '&nbsp; &uarr; ' + oneDayAfterWeather[2] + '&#176; ' + ' | ' + ' &darr; ' + oneDayAfterWeather[3] + '&#176; ');
      forecastDiv.insertAdjacentHTML('beforeend', '<br />' + twoDayAfterWeather[0] + '  ' + '<img src=\"' + twoDayAfterWeather[1] + '\" > ' + '&nbsp; &uarr; ' + twoDayAfterWeather[2] + '&#176; ' + ' | ' + ' &darr; ' + twoDayAfterWeather[3] + '&#176; ');


       
      }
    };

  xhttp.open("GET", "http://127.0.0.1:5000/weather", true);
  xhttp.send();
}

updateTime();
updateDate();

setInterval(updateTime, 3000);
setInterval(updateDate, 60000);

loadWeather();
setInterval(loadWeather, 300000);


