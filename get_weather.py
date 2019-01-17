import requests
import datetime

class WeatherData:

    def __init__(self, api_key, zip_code, temp_format):
        self.api_key = api_key
        self.zip_code = zip_code
        self.temp_format = temp_format
        self.current_conditions_url = 'https://api.openweathermap.org/data/2.5/weather?zip=%s&units=%s&appid=%s' \
            % (self.zip_code, self.temp_format, self.api_key)
        self.forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?zip=%s&units=%s&appid=%s' \
            % (self.zip_code, self.temp_format, self.api_key)

    def get_weather(self):
        weather_reply = []
        weather_reply = [self.get_current_conditions()]
        #weather_reply.extend(self.get_forecast())
        return weather_reply

    def get_current_conditions(self):
        conditions_reply = requests.get(self.current_conditions_url)
        if (conditions_reply.status_code == 200):
            conditions_reply = conditions_reply.json()

            conditions_data = {"temp": conditions_reply["main"]["temp"]}
            conditions_data["location"] = conditions_reply["name"]
            conditions_data["icon"] = conditions_reply["weather"][0]["icon"]

            return conditions_data


    """ def get_forecast(self):
        forecast_reply = requests.get(self.forecast_url)
        if (forecast_reply.status_code == 200):
            forecast_reply = forecast_reply.json()
            

            return [forecast_reply] """
