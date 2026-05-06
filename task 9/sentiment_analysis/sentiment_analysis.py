from textblob import TextBlob

stop_words = {"i", "is", "it", "the", "a", "an", "and", "or", "in", "on",
              "at", "to", "for", "of", "this", "that", "was", "are", "be"}

def preprocess(text):
    tokens = text.lower().split()
    filtered = [w.strip(".,!?") for w in tokens if w.strip(".,!?") not in stop_words]
    return filtered

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        label = "Positive"
    elif polarity < 0:
        label = "Negative"
    else:
        label = "Neutral"

    return polarity, label

reviews = [
    "I love this phone, it works perfectly.",
    "This product is absolutely terrible and broke after one day.",
    "The item is okay, nothing special.",
    "Amazing quality and very fast delivery!",
    "Worst purchase I have ever made.",
    "It is decent but could be better.",
]

print("=" * 55)
print("        Sentiment Analysis using TextBlob + NLTK")
print("=" * 55)

for review in reviews:
    tokens = preprocess(review)
    polarity, label = analyze_sentiment(review)

    print(f"\nReview   : {review}")
    print(f"Tokens   : {tokens}")
    print(f"Polarity : {polarity:.2f}")
    print(f"Sentiment: {label}")
    print("-" * 55)
