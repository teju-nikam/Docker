# ============================================================
# Experiment 4: Docker Volumes - Data Writer
# Writes data to a volume-mounted directory
# ============================================================

import os
import json
from datetime import datetime

DATA_DIR = "/app/data"

def write_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    record = {
        "timestamp": datetime.now().isoformat(),
        "message": "Data written from inside Docker container",
        "container_id": os.environ.get("HOSTNAME", "unknown"),
        "experiment": "Experiment 4 - Docker Volumes"
    }

    filepath = os.path.join(DATA_DIR, "output.json")
    with open(filepath, "w") as f:
        json.dump(record, f, indent=2)

    print(f"[WRITER] Data saved to {filepath}")
    print(f"[WRITER] Content: {json.dumps(record, indent=2)}")

if __name__ == "__main__":
    write_data()
