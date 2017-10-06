from flask import Flask, render_template, jsonify
from getWeather import WeatherData
from getNews import NewsData
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

WEATHER_API_KEY = '' #Paste an API key from a weather service
NEWS_API_KEY = '' #Paste an API key from a news service
ZIP_CODE = '' #Paste your zip code for weather data

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
