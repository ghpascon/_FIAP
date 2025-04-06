from flask import jsonify, request
from main import app,auth
import requests
from bs4 import BeautifulSoup

def get_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        return jsonify({"title": title})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/scrape/title', methods=['GET'])
@auth.login_required
def scrape_title():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    return get_title(url)

def get_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        headers = []
        for header_tag in ['h1', 'h2', 'h3']:
            for header in soup.find_all(header_tag):
                headers.append(header.get_text(strip=True))

        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        return jsonify({"headers": headers, "paragraphs": paragraphs})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/scrape/content', methods=['GET'])
@auth.login_required
def scrape_content():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    return get_content(url)
