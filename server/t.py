import os
from dotenv import load_dotenv
import requests 
import json

load_dotenv()
KEY = os.getenv('NEWSAPI_API_KEY')

url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey={}'
response = requests.get(url.format(KEY))

with open('news.json', 'w') as f:
    json.dump(response.json(), f)
