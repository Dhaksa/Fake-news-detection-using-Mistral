import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

def fetch_headlines(query="", days=1, country="us"):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&q={query}&pageSize=100&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])
