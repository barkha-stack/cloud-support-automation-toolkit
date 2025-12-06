#!/usr/bin/env python3
import sys
import os

# Allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import log_message


def cleanup_logs():
    log_message("Starting cleanup process")

    temp_files = ["logs/temp1.txt", "logs/temp2.txt"]

    for file in temp_files:
        if os.path.exists(file):
            os.remove(file)
            log_message(f"Deleted temp file: {file}")
        else:
            log_message(f"WARNING: Temp file not found: {file}")

    log_message("Cleanup completed successfully")


if __name__ == "__main__":
    cleanup_logs()
