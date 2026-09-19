#!/bin/bash
# ============================================================
# Experiment 3: Containerizing a Python AI Application
# ============================================================

echo "===== Step 1: Build the ML app Docker image ====="
docker build -t ml_iris_app:v1 .

echo ""
echo "===== Step 2: Run the container ====="
docker run --name iris_container ml_iris_app:v1

echo ""
echo "===== Step 3: Validate execution inside container ====="
# Run interactively to explore
# docker run -it --entrypoint bash ml_iris_app:v1

echo ""
echo "===== Step 4: Check container logs ====="
docker logs iris_container

echo ""
echo "===== Step 5: Clean up ====="
docker rm iris_container
docker rmi ml_iris_app:v1

echo ""
echo "===== Experiment 3 Complete! ====="
