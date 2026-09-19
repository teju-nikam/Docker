# ============================================================
# Experiment 6: Multi-Container App using Docker Compose
# Flask web app that connects to a Redis database
# ============================================================

from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis (service name from docker-compose.yml)
REDIS_HOST = os.environ.get("REDIS_HOST", "redis_db")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))

try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r.ping()
    print(f"[APP] Connected to Redis at {REDIS_HOST}:{REDIS_PORT}")
except Exception as e:
    print(f"[APP] Redis connection failed: {e}")
    r = None

@app.route("/")
def home():
    return jsonify({
        "message": "Docker Compose Multi-Container App!",
        "experiment": "Experiment 6",
        "redis_connected": r is not None
    })

@app.route("/count")
def increment_counter():
    if r is None:
        return jsonify({"error": "Redis not connected"}), 500
    count = r.incr("visit_count")
    return jsonify({
        "visit_count": count,
        "message": f"You are visitor #{count}!"
    })

@app.route("/reset")
def reset_counter():
    if r:
        r.set("visit_count", 0)
    return jsonify({"message": "Counter reset to 0"})

@app.route("/health")
def health():
    redis_ok = False
    if r:
        try:
            r.ping()
            redis_ok = True
        except Exception:
            pass
    return jsonify({
        "app_status": "healthy",
        "redis_status": "connected" if redis_ok else "disconnected"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
