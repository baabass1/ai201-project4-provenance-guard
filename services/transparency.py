def generate_transparency_label(llm_score, style_score, confidence, label):
    """
    Generate a transparency report explaining
    how the final decision was made.
    """

    return {
        "final_label": label,
        "confidence_score": confidence,
        "signals": {
            "llm_detector": llm_score,
            "stylometry": style_score
        },
        "explanation": (
            "The final decision combines an AI language model detector "
            "with stylometric writing analysis. Higher confidence indicates "
            "greater agreement between both detection methods."
        )
    }