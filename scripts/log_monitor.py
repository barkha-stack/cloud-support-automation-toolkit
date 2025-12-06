#!/usr/bin/env python3
import sys
import os

# Allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import log_message


def scan_logs():
    log_message("Starting log monitoring")

    log_file = "logs/sample.log"
    output_report = "logs/log_report.txt"

    if not os.path.exists(log_file):
        log_message(f"ERROR: Log file not found: {log_file}")
        return

    issues = []
    keywords = ["ERROR", "WARNING", "CRITICAL", "FAIL"]

    with open(log_file, "r") as f:
        for line in f:
            if any(key in line for key in keywords):
                issues.append(line.strip())

    with open(output_report, "w") as out:
        if issues:
            out.write("\n".join(issues))
        else:
            out.write("No issues found\n")

    log_message("Log scan completed")
    log_message(f"Report saved to: {output_report}")


if __name__ == "__main__":
    scan_logs()
