from flask import Flask, render_template, jsonify
from configparser import ConfigParser
from getWeather import WeatherData
from getNews import NewsData
from flask_cors import CORS, cross_origin

config = ConfigParser()
config.read("./app_config.ini")

app = Flask(__name__)
CORS(app)

WEATHER_API_KEY = config.get("APP_SETTINGS", "weather_api_key")
NEWS_API_KEY = config.get("APP_SETTINGS", "news_api_key")
ZIP_CODE = config.get("APP_SETTINGS", "zip_code")

currentWeather = WeatherData(WEATHER_API_KEY, ZIP_CODE)
currentNews = NewsData(NEWS_API_KEY)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather")
def weather():
    return jsonify(currentWeather.getWeather())

@app.route("/news")
def TOP_NEWS():
    return jsonify(currentNews.getNews())


if __name__ == "__main__":
    app.run()
