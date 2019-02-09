from flask import Flask, render_template, jsonify, request
from configparser import ConfigParser
from get_weather import WeatherData
from get_news import NewsData
from flask_cors import CORS, cross_origin

config = ConfigParser()
config.read("./config/app_config.ini")

app = Flask(__name__)
CORS(app)

WEATHER_API_KEY = config.get("APP_SETTINGS", "weather_api_key")
NEWS_API_KEY = config.get("APP_SETTINGS", "news_api_key")
NEWS_API_URL = config.get("APP_SETTINGS", "news_api_url")

current_weather = WeatherData(WEATHER_API_KEY)
current_news = NewsData(NEWS_API_KEY, NEWS_API_URL)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather")
def weather():
    cookie_data = request.cookies
    return jsonify(current_weather.get_weather(cookie_data["lat"], cookie_data["long"]))

@app.route("/news")
def TOP_NEWS():
    return jsonify(current_news.get_news())


if __name__ == "__main__":
    app.run(host='0.0.0.0')
