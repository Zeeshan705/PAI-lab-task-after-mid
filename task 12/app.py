from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder='static')

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "tinyllama"

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()

    if not user_message:
        return jsonify({'error': 'Message is empty'}), 400

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": user_message,
            "stream": False
        }, timeout=120)

        if response.status_code == 200:
            result = response.json()
            return jsonify({'response': result.get('response', '')})
        else:
            return jsonify({'error': 'Ollama server error'}), 500

    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Ollama not running. Please start Ollama first.'}), 503
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timed out. Model is loading, please try again.'}), 504

@app.route('/api/status', methods=['GET'])
def status():
    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=5)
        if r.status_code == 200:
            models = r.json().get('models', [])
            model_names = [m['name'] for m in models]
            return jsonify({'online': True, 'models': model_names})
    except:
        pass
    return jsonify({'online': False, 'models': []})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
