import requests

def getWeather(api_key):
    weatherReply = []
    weatherReply = [getCurrentConditions(api_key)]
    weatherReply.extend(getForecast(api_key))
    return weatherReply

def getCurrentConditions(api_key):
    r = requests.get('http://api.wunderground.com/api/%s/conditions/q/98684.json' % api_key)
    r = r.json()
    conditionsReply = [r]
    return conditionsReply


def getForecast(api_key):
    r = requests.get('http://api.wunderground.com/api/%s/forecast/q/98684.json' % api_key)
    r = r.json()
    forecastReply = [r]
    return forecastReply