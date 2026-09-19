# ============================================================
# Experiment 7: Dockerfile for ML Model Prediction Service
# ============================================================

FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the saved model and the API server
COPY model.pkl .
COPY predict_api.py .

# Expose the API port
EXPOSE 8000

# Start the prediction API
CMD ["python", "predict_api.py"]
