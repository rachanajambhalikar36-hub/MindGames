from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
CORS(app)

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
# 🗣️ NLP (same as before)
# -------------------------------
from textblob import TextBlob

def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.3:
        return "Happy 😊"
    elif polarity < -0.3:
        return "Sad 😢"
    else:
        return "Neutral 😐"

@app.route("/emotion", methods=["POST"])
def emotion():
    data = request.json
    result = detect_emotion(data["text"])
    return jsonify({"emotion": result})

# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)