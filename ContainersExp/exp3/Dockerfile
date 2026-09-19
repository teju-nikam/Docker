# ============================================================
# Experiment 3: Dockerfile for Python AI/ML Application
# ============================================================

# Base image with Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (Docker layer caching benefit)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ML application
COPY ml_app.py .

# Run the ML application
CMD ["python", "ml_app.py"]
