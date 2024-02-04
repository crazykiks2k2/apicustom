# app.py
import subprocess
import uuid
from flask import Flask, request, jsonify, send_file
import requests
from werkzeug.utils import secure_filename
import os
import ffmpeg
from scipy.spatial import distance


def create_app():
    app = Flask(__name__, static_folder='uploads', static_url_path='/uploads')
    app.config['UPLOAD_FOLDER'] = '/app/uploads/'
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    # Other setup code...
    return app


app = create_app()


@app.route('/', methods=['GET'])
def homepage():
    return "Homepage"


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello"

@app.route('/get_similar', methods=['POST'])
def cosine_similarity():
    data = request.json
    query_vector = data['query_vector']
    vector_text_pairs = data['vectors']

    # Extract embeddings and their corresponding texts
    vectors = [pair['embeddings'] for pair in vector_text_pairs]
    texts = [pair['text'] for pair in vector_text_pairs]

    # Calculate cosine similarity for each vector
    # Return the index of the most similar vector
    most_similar_index = max(range(len(vectors)), key=lambda index: 1 - distance.cosine(query_vector, vectors[index]))

    return jsonify({'most_similar_text': texts[most_similar_index]})


from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def is_trusted_url(url):
    # You can implement your logic to check whether the URL is trusted or fake
    # For simplicity, let's just check if the URL starts with "https://" as an example
    return url.startswith("https://")

@app.route('/check_url', methods=['POST'])
def check_url():
    data = request.get_json()

    if 'url' not in data:
        return jsonify({'error': 'URL not provided'}), 400

    url = data['url']
    is_trusted = is_trusted_url(url)

    return jsonify({'url': url, 'is_trusted': is_trusted})

if __name__ == '__main__':
    app.run(debug=True)

