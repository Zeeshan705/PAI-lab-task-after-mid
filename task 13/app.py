from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import re
import pickle
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r'[^A-Za-z\s]', '', text)
        text = text.lower().strip()
    else:
        text = ''
    return text

df = pd.read_csv('university_qna_clean.csv')
embeddings = np.load('embeddings.npy')

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def retrieve_answers(query, k=5):
    clean_query = clean_text(query)
    query_vec = vectorizer.transform([clean_query]).toarray().astype('float32')
    similarities = cosine_similarity(query_vec, embeddings)[0]
    top_indices = similarities.argsort()[::-1][:k]
    results = []
    for i in top_indices:
        score = float(similarities[i])
        if score > 0:
            results.append({
                'question': df['question'].iloc[i],
                'answer': df['answer'].iloc[i],
                'category': df['category'].iloc[i],
                'score': round(score * 100, 1)
            })
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '').strip()
    if not query:
        return jsonify({'error': 'Please enter a question.'}), 400
    results = retrieve_answers(query)
    if not results:
        return jsonify({'results': [], 'message': 'No relevant answers found.'})
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
