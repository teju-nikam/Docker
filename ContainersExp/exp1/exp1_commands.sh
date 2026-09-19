#!/bin/bash
# ============================================================
# Experiment 1: Installing and Exploring Docker
# ============================================================

echo "===== Step 1: Install Docker on Linux ====="
# Uncomment below lines to install Docker (run once)
# sudo apt-get update
# sudo apt-get install -y docker.io
# sudo systemctl start docker
# sudo systemctl enable docker
# sudo usermod -aG docker $USER    # allow docker without sudo (re-login needed)

echo ""
echo "===== Step 2: Verify Docker Installation ====="
docker --version
docker info | grep -E "Server Version|Operating System|Total Memory"

echo ""
echo "===== Step 3: Explore Docker CLI Commands ====="
echo "-- List local images --"
docker images

echo "-- List running containers --"
docker ps

echo "-- List all containers (including stopped) --"
docker ps -a

echo ""
echo "===== Step 4: Run and Manage Basic Containers ====="

echo "-- Pull hello-world image --"
docker pull hello-world

echo "-- Run hello-world container --"
docker run hello-world

echo "-- Run Nginx web server in detached mode --"
docker run -d -p 8080:80 --name my_nginx nginx
echo "Open http://localhost:8080 in your browser!"

echo "-- View running containers --"
docker ps

echo "-- View container logs --"
docker logs my_nginx

echo "-- Stop and remove container --"
docker stop my_nginx
docker rm my_nginx

echo ""
echo "===== Experiment 1 Complete! ====="
