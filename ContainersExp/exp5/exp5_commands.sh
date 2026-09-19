#!/bin/bash
# ============================================================
# Experiment 5: Docker Networking
# ============================================================

echo "===== Step 1: Create a custom Docker network ====="
docker network create my_custom_network
docker network ls

echo ""
echo "===== Step 2: Inspect the network ====="
docker network inspect my_custom_network

echo ""
echo "===== Step 3: Build server and client images ====="
docker build -f Dockerfile.server -t tcp_server:v1 .
docker build -f Dockerfile.client -t tcp_client:v1 .

echo ""
echo "===== Step 4: Run server on the custom network ====="
docker run -d --name server_container --network my_custom_network tcp_server:v1
echo "Server is running..."
sleep 2

echo ""
echo "===== Step 5: Run client on same network ====="
docker run --rm --name client_container \
  --network my_custom_network \
  -e SERVER_HOST=server_container \
  tcp_client:v1

echo ""
echo "===== Step 6: Inspect container networking ====="
docker inspect server_container | grep -A 10 '"Networks"'

echo ""
echo "===== Step 7: Test DNS resolution between containers ====="
docker run --rm --network my_custom_network alpine \
  ping -c 2 server_container

echo ""
echo "===== Step 8: Clean up ====="
docker stop server_container
docker rm server_container
docker rmi tcp_server:v1 tcp_client:v1
docker network rm my_custom_network

echo ""
echo "===== Experiment 5 Complete! ====="
