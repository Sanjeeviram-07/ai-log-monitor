from app.log_parser import parse_logs
from app.anomaly_detector import detect_anomalies
import datetime

log_file = "logs/sample.log"

logs = parse_logs(log_file)
anomalies = detect_anomalies(logs)

print("---- AI Log Monitoring Report ----")
print("Time:", datetime.datetime.now())
print("-----------------------------------")

if anomalies:
    print("⚠️ Anomalies Detected:")
    for log in anomalies:
        print(f"Severity: {log['severity']} | Message: {log['message']}")
else:
    print("No anomalies found")
