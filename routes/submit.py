from detectors.stylometry import analyze_style
from detectors.confidence import calculate_confidence
from detectors.llm_detector import detect_ai
from flask import Blueprint, request, jsonify

submit_bp = Blueprint("submit", __name__)


@submit_bp.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    text = data.get("text")
    creator_id = data.get("creator_id")

    llm_score = detect_ai(text)
    style_score = analyze_style(text)

    result = calculate_confidence(llm_score, style_score)

    return jsonify({
    "message": "Submission received",
    "text": text,
    "creator_id": creator_id,
    "llm_score": llm_score,
    "style_score": style_score,
    "confidence": result["confidence"],
    "label": result["label"]
    })