"""
Simple logger utility.
This file provides a log_message() function used by all scripts.
"""

import datetime
import os

def log_message(message, log_file="app.log"):
    """
    Writes a timestamped message to the log file.
    Default log file is app.log inside logs/ directory.
    """
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")

    # Ensure logs folder exists
    os.makedirs(logs_dir, exist_ok=True)

    log_path = os.path.join(logs_dir, log_file)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {message}"

    with open(log_path, "a") as f:
        f.write(formatted + "\n")


    return formatted
