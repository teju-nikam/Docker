# ============================================================
# Experiment 7: Containerizing a Machine Learning Model
# Step 2: Flask API that serves the trained model
# ============================================================

from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

MODEL_PATH = "/app/model.pkl"

# Load model at startup
print("[API] Loading trained model...")
try:
    with open(MODEL_PATH, "rb") as f:
        data = pickle.load(f)
    model = data["model"]
    class_names = data["classes"]
    print(f"[API] Model loaded! Classes: {class_names}")
except FileNotFoundError:
    print(f"[API] ERROR: Model file not found at {MODEL_PATH}")
    model = None
    class_names = []

@app.route("/")
def home():
    return jsonify({
        "service": "Iris ML Prediction API",
        "experiment": "Experiment 7 - Containerized ML Model",
        "model_loaded": model is not None,
        "endpoints": {
            "POST /predict": "Predict iris class from features",
            "GET  /health":  "Check API health"
        }
    })

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    try:
        body = request.get_json()
        # Expects: {"features": [5.1, 3.5, 1.4, 0.2]}
        features = np.array(body["features"]).reshape(1, -1)

        pred_idx = model.predict(features)[0]
        pred_proba = model.predict_proba(features)[0]
        confidence = float(pred_proba[pred_idx])

        return jsonify({
            "prediction": class_names[pred_idx],
            "confidence": f"{confidence * 100:.1f}%",
            "input_features": body["features"],
            "all_probabilities": {
                class_names[i]: f"{p * 100:.1f}%"
                for i, p in enumerate(pred_proba)
            }
        })
    except (KeyError, ValueError, TypeError) as e:
        return jsonify({"error": str(e), "expected": "features: [f1, f2, f3, f4]"}), 400

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "model_ready": model is not None
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
