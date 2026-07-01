import json
from datetime import datetime

LOG_FILE = "storage/audit_log.json"


def log_submission(data):
    """Append a submission to the audit log."""

    try:
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    data["timestamp"] = datetime.now().isoformat()

    logs.append(data)

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)