#!/bin/bash
# ============================================================
# Experiment 6: Multi-Container Applications using Docker Compose
# ============================================================

echo "===== Step 1: Start all services with Docker Compose ====="
docker compose up -d --build

echo ""
echo "===== Step 2: Verify all containers are running ====="
docker compose ps

echo ""
echo "===== Step 3: View logs ====="
docker compose logs

echo ""
echo "===== Step 4: Test the application ====="
sleep 3
echo "-- Home endpoint --"
curl http://localhost:5000/

echo ""
echo "-- Visit counter (call multiple times) --"
curl http://localhost:5000/count
curl http://localhost:5000/count
curl http://localhost:5000/count

echo ""
echo "-- Health check --"
curl http://localhost:5000/health

echo ""
echo "===== Step 5: Scale the web app (optional) ====="
# docker compose up -d --scale web_app=3

echo ""
echo "===== Step 6: Stop and remove services ====="
docker compose down -v   # -v also removes named volumes

echo ""
echo "===== Experiment 6 Complete! ====="
