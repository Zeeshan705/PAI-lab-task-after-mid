import pandas as pd
import numpy as np
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r'[^A-Za-z\s]', '', text)
        text = text.lower().strip()
    else:
        text = ''
    return text

df = pd.read_csv('university_qna.csv')
df.dropna(subset=['question', 'answer'], inplace=True)
df['clean_question'] = df['question'].apply(clean_text)
df = df[df['clean_question'].str.strip() != '']
df.reset_index(drop=True, inplace=True)

vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(df['clean_question'].tolist()).toarray().astype('float32')

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

np.save('embeddings.npy', embeddings)
df.to_csv('university_qna_clean.csv', index=False)
print(f"Index built with {len(embeddings)} entries.")
