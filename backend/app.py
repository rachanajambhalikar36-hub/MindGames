from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
CORS(app, origins=["*"], supports_credentials=True)

# -------------------------------
# 📊 TRAINING DATA (fake but valid for project)
# format: [score, time, accuracy]
# -------------------------------
X = [
    [5, 60, 40],
    [10, 50, 55],
    [15, 40, 65],
    [20, 30, 75],
    [25, 20, 85],
    [30, 15, 95]
]

# labels
Y = [
    "Beginner",
    "Beginner",
    "Intermediate",
    "Intermediate",
    "Advanced",
    "Advanced"
]

# -------------------------------
# 🧠 TRAIN MODEL
# -------------------------------
model = DecisionTreeClassifier()
model.fit(X, Y)

# -------------------------------
# 🧠 ML PREDICTION API
# -------------------------------
@app.route("/predict-level", methods=["POST"])
def predict():
    data = request.json

    input_data = [[
        data["score"],
        data["time"],
        data["accuracy"]
    ]]

    prediction = model.predict(input_data)

    return jsonify({
        "level": prediction[0]
    })

# -------------------------------
# 🗣️ NLP (simple sentiment fallback)
# -------------------------------
# Avoids the external TextBlob dependency by using a lightweight keyword-based sentiment heuristic.
POSITIVE_WORDS = {
    "happy", "joy", "love", "awesome", "great", "good", "excited", "nice", "smile",
    "wonderful", "positive", "optimistic", "best"
}
NEGATIVE_WORDS = {
    "sad", "angry", "hate", "bad", "upset", "terrible", "worried", "anxious",
    "stress", "negative", "worst"
}

def detect_emotion(text):
    if not isinstance(text, str) or not text.strip():
        return "Neutral 😐"

    text_lower = text.lower()
    positive_count = sum(word in text_lower for word in POSITIVE_WORDS)
    negative_count = sum(word in text_lower for word in NEGATIVE_WORDS)

    if positive_count > negative_count:
        return "Happy 😊"
    if negative_count > positive_count:
        return "Sad 😢"
    return "Neutral 😐"

@app.route("/emotion", methods=["POST"])
def emotion():
    data = request.json
    result = detect_emotion(data.get("text", ""))
    return jsonify({"emotion": result})

# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
