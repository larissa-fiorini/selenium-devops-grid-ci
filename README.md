# 🎭 Selenium Grid & CI/CD Pipeline Infrastructure

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.20-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-8.0-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
[![Allure Report](https://img.shields.io/badge/Allure_Report-Live-FF6C37?style=for-the-badge&logo=qameta&logoColor=white)](https://larissa-fiorini.github.io/selenium-devops-grid-ci/)

A production-ready test automation framework demonstrating modern DevOps practices for QA. Built with Python and Selenium 4, this repository provides a scalable, containerized execution grid and an automated CI/CD pipeline with live reporting.

Key Features

* Scalable Execution: Configured for cross-browser execution (Chrome & Firefox) and parallel test runs using pytest-xdist.

* Containerized Infrastructure: Includes a docker-compose setup to spin up a local Selenium Grid (Hub + Nodes) with a single command.

* Flexible Architecture: Supports dynamic switching between local drivers and remote execution grids via CLI parameters.

* Automated CI/CD: Integrated GitHub Actions workflow that executes tests on every push or manual trigger.

* Interactive Reporting: Automatically generates Allure Reports with failure screenshots and deploys them to GitHub Pages.

## 🚀 Run locally
### Option 1: Via Docker Compose (Selenium Grid)
```bash
# 1. Grid infrastructure
docker-compose up -d

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run tests on remote Grid
pytest --executor=remote --browser=chrome -n auto
```

### Option 2: Locally on your machine
```bash
# Run all tests using your local browser (Chrome Headless by default)
pytest

# Run tests targeting a specific browser
pytest --browser=firefox

# Run tests in parallel (e.g., using 2 worker processes)
pytest -n 2

# Force a fresh Allure report generation locally
pytest --alluredir=allure-results
allure serve allure-results
```

## 🚀 Run in GitHub Actions (CI/CD Pipeline)
* Go to Actions tab
* Select Test Infrastructure CI/CD from the left sidebar
* Click the Run workflow dropdown on the right.
