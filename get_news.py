import requests

class NewsData:

    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def get_news(self):
        r = requests.get(self.api_url + self.api_key)
        r = r.json()
        news_reply = [r]
        return news_reply