from detectors.llm_detector import detect_ai
from flask import Blueprint, request, jsonify

submit_bp = Blueprint("submit", __name__)


@submit_bp.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    text = data.get("text")
    creator_id = data.get("creator_id")

    ai_score = detect_ai(text)

    return jsonify({
    "message": "Submission received",
    "text": text,
    "creator_id": creator_id,
    "ai_score": ai_score
    })