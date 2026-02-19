import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(logs):
    severities = [log["severity"] for log in logs]
    X = np.array(severities).reshape(-1, 1)

    model = IsolationForest(contamination=0.3, random_state=42)
    model.fit(X)

    predictions = model.predict(X)

    anomalies = []
    for i, prediction in enumerate(predictions):
        if prediction == -1:
            anomalies.append(logs[i])

    return anomalies

