#!/usr/bin/env python3
import sys
import os

# Make parent directory discoverable (so utils/ can be imported)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import log_message
import yaml


def create_sample():
    log_path = "logs/sample.log"
    
    sample_content = [
        "INFO: Application started",
        "WARNING: High memory usage",
        "ERROR: Failed to connect to database",
        "INFO: Application stopped"
    ]
    
    os.makedirs("logs", exist_ok=True)
    
    with open(log_path, "w") as f:
        f.write("\n".join(sample_content))

    log_message(f"Sample log file created at {log_path}")

if __name__ == "__main__":
    create_sample()
