from flask import Blueprint, request, jsonify
import json
from datetime import datetime

appeal_bp = Blueprint("appeal", __name__)

APPEALS_FILE = "storage/appeals.json"


@appeal_bp.route("/appeal", methods=["POST"])
def submit_appeal():
    data = request.get_json()

    creator_id = data.get("creator_id")
    reason = data.get("reason")

    try:
        with open(APPEALS_FILE, "r") as file:
            appeals = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        appeals = []

    appeal = {
        "creator_id": creator_id,
        "reason": reason,
        "timestamp": datetime.now().isoformat(),
        "status": "Pending"
    }

    appeals.append(appeal)

    with open(APPEALS_FILE, "w") as file:
        json.dump(appeals, file, indent=4)

    return jsonify({
        "message": "Appeal submitted successfully.",
        "appeal": appeal
    })