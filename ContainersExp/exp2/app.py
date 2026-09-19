# ============================================================
# Experiment 2: Creating and Managing Docker Images
# Simple Python application to containerize
# ============================================================
import platform
import sys

def greet():
    print("=" * 50)
    print("  Hello from inside a Docker Container!")
    print("=" * 50)
    print(f"  Python Version : {sys.version.split()[0]}")
    print(f"  Platform       : {platform.system()} {platform.release()}")
    print(f"  Architecture   : {platform.machine()}")
    print("=" * 50)
    print("  Docker image built successfully!")
    print("=" * 50)

if __name__ == "__main__":
    greet()
