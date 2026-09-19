#!/bin/bash
# ============================================================
# Experiment 4: Managing Docker Volumes and Persistent Storage
# ============================================================

echo "===== Step 1: Create a Named Docker Volume ====="
docker volume create my_data_volume
docker volume ls

echo ""
echo "===== Step 2: Inspect the volume ====="
docker volume inspect my_data_volume

echo ""
echo "===== Step 3: Build writer and reader images ====="
docker build -f Dockerfile.writer -t data_writer:v1 .
docker build -f Dockerfile.reader -t data_reader:v1 .

echo ""
echo "===== Step 4: Run writer — stores data in the volume ====="
docker run --name writer_container -v my_data_volume:/app/data data_writer:v1

echo ""
echo "===== Step 5: Run reader — reads from same volume ====="
docker run --name reader_container -v my_data_volume:/app/data data_reader:v1

echo ""
echo "===== Step 6: Bind Mount example ====="
mkdir -p ./host_data
docker run --rm -v $(pwd)/host_data:/app/data data_writer:v1
echo "Files on host:"
ls ./host_data/

echo ""
echo "===== Step 7: Compare bind mount vs named volume ====="
echo "Named volume: managed by Docker, lives in Docker area"
echo "Bind mount  : links a host directory directly into container"

echo ""
echo "===== Step 8: Clean up ====="
docker rm writer_container reader_container
docker rmi data_writer:v1 data_reader:v1
docker volume rm my_data_volume

echo ""
echo "===== Experiment 4 Complete! ====="
