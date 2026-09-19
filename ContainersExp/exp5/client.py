# ============================================================
# Experiment 5: Docker Networking — Simple TCP Client
# Connects to the server container and sends a message
# ============================================================

import socket
import os
import sys

SERVER_HOST = os.environ.get("SERVER_HOST", "server_container")
SERVER_PORT = int(os.environ.get("SERVER_PORT", "5000"))

def connect_to_server():
    message = "Ping from client container!"
    print(f"[CLIENT] Connecting to {SERVER_HOST}:{SERVER_PORT}")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_HOST, SERVER_PORT))
            s.sendall(message.encode())
            response = s.recv(1024).decode()
            print(f"[CLIENT] Response: {response}")
            print("[CLIENT] Inter-container communication SUCCESS!")
    except ConnectionRefusedError:
        print(f"[CLIENT] Could not connect to {SERVER_HOST}:{SERVER_PORT}")
        print("[CLIENT] Make sure server container is running on the same network!")
        sys.exit(1)

if __name__ == "__main__":
    connect_to_server()
