![CI](https://github.com/barkha-stack/cloud-support-automation-toolkit/actions/workflows/ci.yml/badge.svg)

# Cloud Support Automation Toolkit

# Cloud Support Automation Toolkit

A beginner-friendly Python automation project that simulates real-world
Cloud Support / DevOps tasks such as log monitoring, health checks,
cleanup jobs, and CI/CD automation.

---

## ✅ Features

- Log generation and monitoring
- Centralized logging using a shared utility
- Health checks (system disk usage)
- Cleanup automation
- Master script to run all tasks
- CI/CD with GitHub Actions

---

## 📂 Project Structure

cloud-support-automation-toolkit/
├── scripts/
│ ├── create_sample_log.py
│ ├── log_monitor.py
│ ├── health_check.py
│ ├── cleanup_resources.py
│ └── master_script.py
├── utils/
│ └── logger.py
├── config/
│ └── config.yaml
├── .github/workflows/
│ └── ci.yml
├── .gitignore
├── requirements.txt
└── README.md

---

## 🚀 How to Run

Run the entire toolkit with one command:

python scripts/master_script.py

Logs will be generated automatically inside the logs/ folder.

🧪 CI/CD
This project uses GitHub Actions to automatically:
Set up Python
Install dependencies
Run all automation scripts on every push

Use Case (Real Life)

This project demonstrates how cloud support engineers:
Monitor logs for errors and warnings
Run periodic health checks
Automate routine cleanup tasks
Use CI/CD to validate automation scripts