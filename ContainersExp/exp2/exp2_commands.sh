#!/bin/bash
# ============================================================
# Experiment 2: Creating and Managing Docker Images
# ============================================================

echo "===== Step 1: Pull images from Docker Hub ====="
docker pull python:3.11-slim
docker pull ubuntu:22.04
docker images

echo ""
echo "===== Step 2: Build our custom Docker image ====="
# Run from the exp2 directory
docker build -t my_python_app:v1 .

echo ""
echo "===== Step 3: Run the custom image ====="
docker run --name python_container my_python_app:v1

echo ""
echo "===== Step 4: Tag the image ====="
docker tag my_python_app:v1 my_python_app:latest
docker images

echo ""
echo "===== Step 5: Inspect the image ====="
docker inspect my_python_app:v1

echo ""
echo "===== Step 6: View image layer history ====="
docker history my_python_app:v1

echo ""
echo "===== Step 7: Remove container and image ====="
docker rm python_container
docker rmi my_python_app:latest my_python_app:v1

echo ""
echo "===== Experiment 2 Complete! ====="
