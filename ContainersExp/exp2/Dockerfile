# ============================================================
# Experiment 2: Dockerfile for Python Application
# ============================================================

# Step 1: Base image
FROM python:3.11-slim

# Step 2: Working directory inside container
WORKDIR /app

# Step 3: Copy app files into the container
COPY app.py .

# Step 4: Install dependencies (none here, but shown for reference)
# RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Command to run on container start
CMD ["python", "app.py"]
