import requests

class NewsData:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_news(self):
        r = requests.get('https://newsapi.org/v1/articles?source=google-news&sortBy=top&apiKey=%s' % self.api_key)
        r = r.json()
        news_reply = [r]
        return news_reply