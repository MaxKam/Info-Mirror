import requests

class WeatherData:

    def __init__(self, api_key, zip_code, temp_format):
        self.api_key = api_key
        self.zip_code = zip_code
        self.temp_format = temp_format

    def get_weather(self):
        weather_reply = []
        weather_reply = [self.get_current_conditions()]
        weather_reply.extend(self.get_forecast())
        return weather_reply

    def get_current_conditions(self):
        conditions_reply = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=%s&units=%s&appid=%s' % (self.zip_code, self.temp_format, self.api_key))
        conditions_reply = conditions_reply.json()
        conditions_reply = [conditions_reply]
        return conditions_reply


    def get_forecast(self):
        forecast_reply = requests.get('https://api.openweathermap.org/data/2.5/forecast?zip=%s&units=%s&appid=%s' % (self.zip_code, self.temp_format, self.api_key))
        forecast_reply = forecast_reply.json()
        forecast_reply = [forecast_reply]
        return forecast_reply