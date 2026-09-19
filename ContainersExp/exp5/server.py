# ============================================================
# Experiment 5: Docker Networking — Simple TCP Server
# Listens on port 5000 and responds to messages
# ============================================================

import socket
import threading
import os

HOST = "0.0.0.0"
PORT = 5000
CONTAINER_NAME = os.environ.get("HOSTNAME", "server")

def handle_client(conn, addr):
    print(f"[SERVER] Connection from {addr}")
    data = conn.recv(1024).decode()
    print(f"[SERVER] Received: {data}")
    response = f"Hello from Docker container '{CONTAINER_NAME}'! You sent: '{data}'"
    conn.sendall(response.encode())
    conn.close()

def start_server():
    print(f"[SERVER] Starting on {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"[SERVER] Listening... (container: {CONTAINER_NAME})")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
