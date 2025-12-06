#!/usr/bin/env python3
import sys
import os
import shutil
import platform

# Allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import log_message


# Thresholds (real-world reasonable defaults)
DISK_WARNING_THRESHOLD = 80  # percent


def check_disk_usage():
    """Check disk usage of the current system."""
    total, used, free = shutil.disk_usage(os.getcwd())
    usage_percent = round((used / total) * 100, 2)

    log_message(f"Disk usage: {usage_percent}%")

    if usage_percent >= DISK_WARNING_THRESHOLD:
        log_message("WARNING: Disk usage above threshold")


def check_system_info():
    """Log basic system information."""
    log_message(f"Operating System: {platform.system()} {platform.release()}")
    log_message(f"Architecture: {platform.machine()}")


def health_check():
    log_message("Starting system health check")

    check_system_info()
    check_disk_usage()

    log_message("System health check completed successfully")


if __name__ == "__main__":
    health_check()
