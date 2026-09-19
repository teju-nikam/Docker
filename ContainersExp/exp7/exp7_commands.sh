#!/bin/bash
# ============================================================
# Experiment 7: Containerizing a Machine Learning Model
# ============================================================

echo "===== Step 1: Install dependencies locally & train model ====="
pip install scikit-learn==1.4.2 numpy==1.26.4 --quiet
python train_model.py

echo ""
echo "===== Step 2: Build the Docker image (includes model.pkl) ====="
docker build -t ml_api:v1 .

echo ""
echo "===== Step 3: Run the containerized ML API ====="
docker run -d -p 8000:8000 --name ml_api_container ml_api:v1
sleep 2

echo ""
echo "===== Step 4: Test inference with API requests ====="

echo "-- Home endpoint --"
curl http://localhost:8000/

echo ""
echo "-- Health check --"
curl http://localhost:8000/health

echo ""
echo "-- Prediction (Iris Setosa sample) --"
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

echo ""
echo "-- Prediction (Iris Versicolor sample) --"
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [6.0, 2.9, 4.5, 1.5]}'

echo ""
echo "-- Prediction (Iris Virginica sample) --"
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [6.7, 3.1, 5.6, 2.4]}'

echo ""
echo "===== Step 5: View container logs ====="
docker logs ml_api_container

echo ""
echo "===== Step 6: Clean up ====="
docker stop ml_api_container
docker rm ml_api_container
docker rmi ml_api:v1

echo ""
echo "===== Experiment 7 Complete! ====="
