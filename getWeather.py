import requests

class WeatherData:

    def __init__(self, api_key, zip_code):
        self.api_key = api_key
        self.zip_code = zip_code

    def getWeather(self):
        weatherReply = []
        weatherReply = [self.getCurrentConditions()]
        weatherReply.extend(self.getForecast())
        return weatherReply

    def getCurrentConditions(self):
        r = requests.get('http://api.wunderground.com/api/%s/conditions/q/%s.json' % (self.api_key, self.zip_code))
        r = r.json()
        conditionsReply = [r]
        return conditionsReply


    def getForecast(self):
        r = requests.get('http://api.wunderground.com/api/%s/forecast/q/%s.json' % (self.api_key, self.zip_code))
        r = r.json()
        forecastReply = [r]
        return forecastReply