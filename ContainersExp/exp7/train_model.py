# ============================================================
# Experiment 7: Containerizing a Machine Learning Model
# Step 1: Train and save the model
# Run this BEFORE building the Docker image
# ============================================================

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os

MODEL_PATH = "model.pkl"

def train_and_save():
    print("[TRAINER] Loading Iris dataset...")
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("[TRAINER] Training RandomForestClassifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"[TRAINER] Accuracy: {acc * 100:.2f}%")

    with open(MODEL_PATH, "wb") as f:
        pickle.dump({"model": model, "classes": iris.target_names.tolist()}, f)

    print(f"[TRAINER] Model saved to {MODEL_PATH}")
    print("[TRAINER] Now build the Docker image!")

if __name__ == "__main__":
    train_and_save()
