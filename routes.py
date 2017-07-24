from flask import Flask, render_template, jsonify
from getWeather import getWeather
from getNews import getTopNews
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

WEATHER_API_KEY = '' #Paste an API key from a weather service
NEWS_API_KEY = '' #Paste an API key from a news service

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather")
def weather():
    fullWeatherReply = getWeather(WEATHER_API_KEY)
    return jsonify(fullWeatherReply)

@app.route("/news")
def TOP_NEWS():
    newsReply = getTopNews(NEWS_API_KEY)
    return jsonify(newsReply)


if __name__ == "__main__":
    app.run()
