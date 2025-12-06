#!/usr/bin/env python3
import sys
import os
import shutil

# Allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import log_message


def health_check():
    log_message("Starting health check")

    total, used, free = shutil.disk_usage(os.getcwd())
    usage_percent = round((used / total) * 100, 2)

    log_message(f"Disk usage: {usage_percent}%")

    if usage_percent > 80:
        log_message("WARNING: Disk usage above threshold")

    log_message("Health check completed successfully")


if __name__ == "__main__":
    health_check()
