# fetches news using NewsAPI 
from flask import Flask, jsonify
from flask_cors import CORS
import requests
import sqlite3
import os
from dotenv import load_dotenv
import json

load_dotenv()
KEY = os.getenv('NEWSAPI_API_KEY')

app = Flask(__name__)
CORS(app)

# Initialize the SQLite database
db = sqlite3.connect('news.db')
db.execute('CREATE TABLE IF NOT EXISTS news (title TEXT, description TEXT, publishedAt TIMESTAMP, imgSrc TEXT, source TEXT, url TEXT, country TEXT)')
db.commit()
db.close()

with open('../src/countries.json') as f:
    countries = json.load(f)
    
@app.route('/fetch-news', methods=['GET'])
def fetch_news():
    try:
        # Store articles in the database
        db = sqlite3.connect('news.db')
        db.execute('CREATE UNIQUE INDEX IF NOT EXISTS title ON news (title)')
        cursor = db.cursor()

        # Fetch news articles from NewsAPI
        url = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'

        # fetch news for each country
        for country in countries:
            response = requests.get(url.format(country, KEY))
            print(response.json())
            articles = response.json()['articles']
            cursor.executemany('INSERT OR IGNORE INTO news VALUES (?, ?, ?, ?, ?, ?, ?)', [(article['title'], article['description'], article['publishedAt'], article['urlToImage'], article['source']['name'], article['url'], country) for article in articles])

        db.commit()
        db.close()

        return jsonify({'message': 'News fetched and stored successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/get-news', methods=['GET'])
def get_news():
    try:
        db = sqlite3.connect('news.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM news')
        # fetch as a list of dictionaries
        news = [{'title': row[0], 'description': row[1], 'publishedAt': row[2], 'imgSrc': row[3], 'source': row[4], 'url': row[5], 'country': row[6]} for row in cursor.fetchall()]
        news.sort(key=lambda x: x['publishedAt'], reverse=True)
        db.close()
        return jsonify(news)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
