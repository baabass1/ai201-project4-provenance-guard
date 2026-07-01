from flask import Blueprint, jsonify
import json

logs_bp = Blueprint("logs", __name__)


@logs_bp.route("/logs", methods=["GET"])
def get_logs():
    try:
        with open("storage/audit_log.json", "r") as file:
            logs = json.load(file)
    except Exception:
        logs = []

    return jsonify(logs)