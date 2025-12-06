import subprocess
import os

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    print(f"\n🔹 Running {script_name}...")
    result = subprocess.run(["python", script_path])
    
    if result.returncode == 0:
        print(f"✅ {script_name} completed successfully!")
    else:
        print(f"❌ Error running {script_name}")

def main():
    print("🚀 Starting Cloud Support Automation Toolkit\n")

    run_script("create_sample_log.py")
    run_script("log_monitor.py")
    run_script("health_check.py")
    run_script("cleanup_resources.py")

    print("\n🎉 All tasks completed!")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import sys
import os
import subprocess

# Allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import log_message

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def run_script(script_name):
    """Runs a script and logs its execution"""
    script_path = os.path.join(SCRIPTS_DIR, script_name)

    log_message(f"Starting {script_name}")

    result = subprocess.run(
        ["python", script_path],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        log_message(f"{script_name} completed successfully")
    else:
        log_message(f"ERROR: {script_name} failed")
        log_message(result.stderr)


def main():
    log_message("=== Starting Cloud Support Automation Toolkit ===")

    run_script("create_sample_log.py")
    run_script("log_monitor.py")
    run_script("health_check.py")
    run_script("cleanup_resources.py")

    log_message("=== Cloud Support Automation Toolkit Finished ===")


if __name__ == "__main__":
    main()
