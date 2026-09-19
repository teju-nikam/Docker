# ============================================================
# Experiment 3: Containerizing a Python AI Application
# Simple ML app: Iris flower classifier using scikit-learn
# ============================================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

def train_and_predict():
    print("=" * 55)
    print("  Iris Flower Classifier — Running in Docker!")
    print("=" * 55)

    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    class_names = iris.target_names

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    print("\n[1] Training RandomForestClassifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("    Training complete!")

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\n[2] Accuracy on test set: {acc * 100:.2f}%")

    print("\n[3] Classification Report:")
    print(classification_report(y_test, y_pred, target_names=class_names))

    # Predict on a new sample
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # typical setosa
    prediction = model.predict(sample)
    print(f"[4] Sample prediction for {sample.tolist()}:")
    print(f"    Predicted class: {class_names[prediction[0]]}")

    print("\n" + "=" * 55)
    print("  ML app ran successfully inside Docker container!")
    print("=" * 55)

if __name__ == "__main__":
    train_and_predict()
