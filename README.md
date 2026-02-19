#  AI Log Monitoring Microservice

An AI-powered log anomaly detection microservice built using FastAPI and Isolation Forest.  
Fully containerized with Docker and integrated with CI/CD using GitHub Actions.

---

##  Project Overview

This project detects anomalies in log data using Machine Learning and exposes the functionality via a REST API.

The application is:

- > Built with FastAPI
- > Powered by Isolation Forest (Scikit-Learn)
- > Containerized using Docker
- > Automated testing using Pytest
- > CI/CD pipeline using GitHub Actions
- > Docker image publishing support

---

##  Architecture

Client → FastAPI REST API → ML Model (Isolation Forest) → Anomaly Prediction

CI/CD Flow:

Push to GitHub → GitHub Actions → Run Tests → Build Docker Image → Push to Docker Hub

---

##  Tech Stack

- Python 3.12
- FastAPI
- Scikit-learn
- Pytest
- Docker
- GitHub Actions

---

##  Project Structure

ai-log-monitor/
│
├── app/
│ ├── init.py
│ ├── api.py
│ └── model.py
│
├── tests/
│ └── test_basic.py
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── .github/workflows/ci.yml


---

##  Running Locally

###  Clone Repository

```bash
git clone https://github.com/Sanjeeviram-07/ai-log-monitor.git
cd ai-log-monitor
### **Create Virtual Environment**
python3 -m venv venv
source venv/bin/activate
**Install Dependencies**
**pip install -r requirements.txt
 Run API**
uvicorn app.api:app --reload
**Open in browser:**
http://localhost:8000/docs

**Run Using Docker**
**Build Image**
docker build -t ai-log-monitor .
**Run Container**
docker run -p 8000:8000 ai-log-monitor
** CI/CD Pipeline**
This project uses GitHub Actions to:
>
Install dependencies
>
Run automated tests
>
Build Docker image
>
Push Docker image to Docker Hub
>
The pipeline runs automatically on every push to the main branch.

- >**Future Improvements**
Add Prometheus metrics

Add structured logging

Deploy to AWS / Render

Add React-based dashboard UI

Add real-time log ingestion pipeline

** License**
This project is open-source for learning and portfolio purposes.
