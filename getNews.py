import requests

def getTopNews(api_key):
    r = requests.get('https://newsapi.org/v1/articles?source=google-news&sortBy=top&apiKey=%s' % api_key)
    r = r.json()
    newsReply = [r]
    return newsReply