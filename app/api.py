from fastapi import FastAPI, UploadFile, File
from app.log_parser import parse_logs
from app.anomaly_detector import detect_anomalies
import shutil
import os

app = FastAPI()

UPLOAD_PATH = "logs/uploaded.log"

@app.get("/")
def home():
    return {"message": "AI Log Monitoring API Running"}

@app.post("/analyze-log/")
async def analyze_log(file: UploadFile = File(...)):
    with open(UPLOAD_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logs = parse_logs(UPLOAD_PATH)
    anomalies = detect_anomalies(logs)

    return {
        "total_logs": len(logs),
        "anomalies_detected": len(anomalies),
        "anomaly_details": anomalies
    }

