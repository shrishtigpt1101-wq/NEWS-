'''
This app will fetch the latest headlines, display articles, and allow users to filter news based on categories or keywords. 
It helps you practice working with APIs, handling JSON data, and building user interfaces.
'''

import requests # pip install requests
from datetime import datetime, timedelta

query = input("What type of news are you interested in today? ")
api = "2e59ee9159a14863987e30bfa10109a7"

from_date = (datetime.now() - timedelta(days=30)).date().isoformat()
url = f"https://newsapi.org/v2/everything?q={query}&from={from_date}&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
if data.get("status") != "ok":
    print("NewsAPI error:", data.get("message", data))
    raise SystemExit(1)

articles = data.get("articles", [])
if not articles:
    print("No articles found for that query.")

for index, article in enumerate(articles):
    print(index + 1, article.get("title", "No title"), article.get("url", "No URL"))
    print("\n****************************************\n")
