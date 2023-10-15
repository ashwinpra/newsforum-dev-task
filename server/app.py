# fetches news using NewsAPI 
from flask import Flask, jsonify
from flask_cors import CORS
import requests
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('NEWSAPI_API_KEY')

app = Flask(__name__)
CORS(app)

# Initialize the SQLite database
db = sqlite3.connect('news.db')
db.execute('CREATE TABLE IF NOT EXISTS news (title TEXT, description TEXT, imgSrc TEXT, source TEXT, url TEXT)')
db.commit()
db.close()

@app.route('/fetch-news', methods=['GET'])
def fetch_news():
    try:
        # Fetch news articles from NewsAPI
        url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey={}'
        response = requests.get(url.format(KEY))
        articles = response.json().get('articles', [])

        # Store articles in the database
        db = sqlite3.connect('news.db')
        db.execute('CREATE UNIQUE INDEX IF NOT EXISTS title ON news (title)')
        cursor = db.cursor()
        for article in articles: 
            try: 
                cursor.execute('INSERT INTO news (title, description, imgSrc, source, url) VALUES (?, ?, ?, ?, ?)', (article['title'], article['description'], article['urlToImage'], article['source']['name'], article['url']))
            except sqlite3.IntegrityError:
                pass
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
        news = [{'title': row[0], 'description': row[1], 'imgSrc': row[2], 'source': row[3], 'url': row[4]} for row in cursor.fetchall()]
        db.close()
        return jsonify(news)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
