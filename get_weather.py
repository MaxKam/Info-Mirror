import requests

class WeatherData:

    def __init__(self, api_key, zip_code):
        self.api_key = api_key
        self.zip_code = zip_code

    def get_weather(self):
        weather_reply = []
        weather_reply = [self.get_current_conditions()]
        weather_reply.extend(self.get_forecast())
        return weather_reply

    def get_current_conditions(self):
        conditions_reply = requests.get('http://api.wunderground.com/api/%s/conditions/q/%s.json' % (self.api_key, self.zip_code))
        conditions_reply = conditions_reply.json()
        conditions_reply = [conditions_reply]
        return conditions_reply


    def get_forecast(self):
        forecast_reply = requests.get('http://api.wunderground.com/api/%s/forecast/q/%s.json' % (self.api_key, self.zip_code))
        forecast_reply = forecast_reply.json()
        forecast_reply = [forecast_reply]
        return forecast_reply