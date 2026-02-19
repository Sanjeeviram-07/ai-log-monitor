# 🧠 AI Log Monitoring Microservice

An AI-powered log anomaly detection microservice built with **FastAPI**
and **Isolation Forest**.\
Fully containerized using **Docker** and automated with **CI/CD (GitHub
Actions)** --- perfect for learning, demos, and portfolio projects.

------------------------------------------------------------------------

## 🚀 Project Overview

This service detects anomalies in application/system logs using Machine
Learning and exposes predictions through a REST API.

### ✨ Key Features

-   ⚡ FastAPI-based REST API
-   🤖 ML-powered anomaly detection (Isolation Forest -- Scikit-learn)
-   🐳 Dockerized for easy deployment
-   🧪 Automated testing with Pytest
-   🔄 CI/CD pipeline with GitHub Actions
-   📦 Docker image build & publish support

------------------------------------------------------------------------

## 🏗️ Architecture

**Request Flow**\
Client → FastAPI REST API → ML Model (Isolation Forest) → Anomaly
Prediction

**CI/CD Flow**\
Push to GitHub → GitHub Actions → Run Tests → Build Docker Image → Push
to Docker Hub

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python 3.12\
-   FastAPI\
-   Scikit-learn\
-   Pytest\
-   Docker\
-   GitHub Actions

------------------------------------------------------------------------

## 📁 Project Structure

    ai-log-monitor/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── api.py
    │   └── model.py
    │
    ├── tests/
    │   └── test_basic.py
    │
    ├── Dockerfile
    ├── requirements.txt
    ├── pytest.ini
    └── .github/workflows/ci.yml

------------------------------------------------------------------------

## 🧑‍💻 Running Locally

### 1️⃣ Clone Repository

``` bash
git clone https://github.com/Sanjeeviram-07/ai-log-monitor.git
cd ai-log-monitor
```

### 2️⃣ Create Virtual Environment

``` bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Run API

``` bash
uvicorn app.api:app --reload
```

📌 Open Swagger UI:\
👉 http://localhost:8000/docs

------------------------------------------------------------------------

## 🐳 Run Using Docker

### Build Image

``` bash
docker build -t ai-log-monitor .
```

### Run Container

``` bash
docker run -p 8000:8000 ai-log-monitor
```

------------------------------------------------------------------------

## 🔄 CI/CD Pipeline

This project uses **GitHub Actions** to automatically:

-   Install dependencies\
-   Run Pytest\
-   Build Docker image\
-   Push image to Docker Hub

The pipeline runs on every push to the **main** branch.

------------------------------------------------------------------------

## 🔮 Future Improvements

-   📊 Add Prometheus metrics\
-   🪵 Add structured logging\
-   ☁️ Deploy to AWS / Render\
-   🖥️ Add React-based dashboard UI\
-   🔁 Real-time log ingestion pipeline (Kafka / Fluentd)

------------------------------------------------------------------------

## 📜 License

This project is open-source and intended for **learning and portfolio
purposes**.

------------------------------------------------------------------------

⭐ If you found this useful, feel free to star the repository!
