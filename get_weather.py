import requests
import datetime

class WeatherData:

    def __init__(self, api_key, latitude, longitude):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.request_url = 'https://api.darksky.net/forecast/%s/%s,%s?exclude=minutely,hourly,flags' \
            % (self.api_key, self.latitude, self.longitude )

    def get_weather(self):
        weather_reply = []

        conditions_request = requests.get(self.request_url)
        if (conditions_request.status_code == 200):
            conditions_request = conditions_request.json()

            weather_reply = [self.extract_current_conditions(conditions_request)]
            weather_reply.append(self.extract_forecast(conditions_request))
            return weather_reply

    def extract_current_conditions(self, raw_data):
        conditions_data = {}
        conditions_data["temp"] = raw_data["currently"]["temperature"]
        conditions_data["feels_like"] = raw_data["currently"]["apparentTemperature"]
        conditions_data["icon"] = raw_data["currently"]["icon"]
        conditions_data["summary"] = raw_data["currently"]["summary"]
        return conditions_data


    def extract_forecast(self, raw_data):
        conditions_data = {}
        conditions_data["todays_high"] = raw_data["daily"]["data"][0]["temperatureHigh"]
        conditions_data["todays_low"] = raw_data["daily"]["data"][0]["temperatureLow"]
        
        conditions_data["day1_icon"] = raw_data["daily"]["data"][1]["icon"]
        conditions_data["day1_high"] = raw_data["daily"]["data"][1]["temperatureHigh"]
        conditions_data["day1_low"] = raw_data["daily"]["data"][1]["temperatureLow"]

        conditions_data["day2_icon"] = raw_data["daily"]["data"][2]["icon"]
        conditions_data["day2_high"] = raw_data["daily"]["data"][2]["temperatureHigh"]
        conditions_data["day2_low"] = raw_data["daily"]["data"][2]["temperatureLow"]

        conditions_data["day3_icon"] = raw_data["daily"]["data"][3]["icon"]
        conditions_data["day3_high"] = raw_data["daily"]["data"][3]["temperatureHigh"]
        conditions_data["day3_low"] = raw_data["daily"]["data"][3]["temperatureLow"]

        return conditions_data

