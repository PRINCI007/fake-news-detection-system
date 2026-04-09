# app.py

from flask import Flask, request, jsonify
import pickle
import re
import string

app = Flask(__name__)

# 🔹 Load model and vectorizer
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))


# 🔹 Text cleaning (same as train.py)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text


# 🔹 API Route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    cleaned = clean_text(text)
    vect = vectorizer.transform([cleaned])

    prediction = model.predict(vect)[0]
    probability = model.predict_proba(vect)[0]

    confidence = max(probability) * 100

    return jsonify({
        "prediction": "Real" if prediction == 1 else "Fake",
        "confidence": f"{confidence:.2f}%"
    })


# 🔹 Run server
if __name__ == "__main__":
    app.run(debug=True, port=5000)