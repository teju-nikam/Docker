# ============================================================
# Experiment 4: Docker Volumes - Data Reader
# Reads data from a volume-mounted directory
# ============================================================

import os
import json

DATA_DIR = "/app/data"

def read_data():
    filepath = os.path.join(DATA_DIR, "output.json")

    if not os.path.exists(filepath):
        print(f"[READER] No data found at {filepath}")
        print("[READER] Run the writer container first!")
        return

    with open(filepath, "r") as f:
        record = json.load(f)

    print(f"[READER] Successfully read data from volume!")
    print(f"[READER] Content: {json.dumps(record, indent=2)}")
    print("[READER] Data persisted across container runs!")

if __name__ == "__main__":
    read_data()
