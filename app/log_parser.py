def parse_logs(file_path):
    logs = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        if "ERROR" in line:
            severity = 3
        elif "WARNING" in line:
            severity = 2
        else:
            severity = 1

        logs.append({
            "message": line.strip(),
            "severity": severity
        })

    return logs


