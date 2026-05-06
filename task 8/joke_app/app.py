from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_joke')
def get_joke():
    response = requests.get(
        'https://official-joke-api.appspot.com/random_joke',
        timeout=5
    )
    data = response.json()
    return jsonify({
        'setup': data['setup'],
        'punchline': data['punchline'],
        'type': data['type']
    })

@app.route('/get_joke/<category>')
def get_joke_by_category(category):
    response = requests.get(
        f'https://official-joke-api.appspot.com/jokes/{category}/random',
        timeout=5
    )
    data = response.json()
    if isinstance(data, list):
        data = data[0]
    return jsonify({
        'setup': data['setup'],
        'punchline': data['punchline'],
        'type': data['type']
    })

if __name__ == '__main__':
    app.run(debug=True)
