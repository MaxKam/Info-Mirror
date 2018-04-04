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
        r = requests.get('http://api.wunderground.com/api/%s/conditions/q/%s.json' % (self.api_key, self.zip_code))
        r = r.json()
        conditions_reply = [r]
        return conditions_reply


    def get_forecast(self):
        r = requests.get('http://api.wunderground.com/api/%s/forecast/q/%s.json' % (self.api_key, self.zip_code))
        r = r.json()
        forecast_reply = [r]
        return forecast_reply