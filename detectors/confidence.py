def calculate_confidence(llm_score, style_score):
    """
    Combine the LLM score and stylometry score
    into a single confidence score.
    """

    confidence = round((llm_score + style_score) / 2)

    if confidence >= 70:
        label = "Likely AI"

    elif confidence <= 30:
        label = "Likely Human"

    else:
        label = "Uncertain"

    return {
        "confidence": confidence,
        "label": label
    }