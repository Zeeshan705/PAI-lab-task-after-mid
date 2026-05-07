# 🔒 PrivateAI — Setup Guide

## Step 1: Ollama Install karo
https://ollama.com se download karo (Windows/Mac/Linux sab ke liye hai)

## Step 2: Mistral model download karo
```bash
ollama pull mistral
```
> ~4GB download hoga — ek baar, phir offline kaam karta hai

## Step 3: Python dependencies install karo
```bash
pip install -r requirements.txt
```

## Step 4: App chalao
```bash
# Terminal 1 — Ollama server
ollama serve

# Terminal 2 — Flask app
python app.py
```

## Step 5: Browser mein kholo
```
http://localhost:5000
```

---
## Project Structure
```
llm-app/
├── app.py            ← Flask backend
├── requirements.txt  ← Dependencies
└── static/
    └── index.html    ← Frontend UI
```

## Endpoints
- `GET  /`           → Frontend UI
- `POST /api/chat`   → Send message to LLM
- `GET  /api/status` → Check Ollama status
