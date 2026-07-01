import re


def analyze_style(text):
    """
    Analyze basic writing style features.
    Returns a score between 0 and 100,
    where higher means more AI-like.
    """

    words = text.split()
    sentences = re.split(r"[.!?]+", text)

    # Remove empty sentences
    sentences = [s for s in sentences if s.strip()]

    if not words or not sentences:
        return 50

    average_sentence_length = len(words) / len(sentences)

    unique_words = len(set(word.lower() for word in words))
    vocabulary_diversity = unique_words / len(words)

    score = 0

    # Long, consistent sentences tend to be more AI-like
    if average_sentence_length > 20:
        score += 40
    elif average_sentence_length > 15:
        score += 25
    else:
        score += 10

    # Very high vocabulary diversity can indicate AI
    if vocabulary_diversity > 0.8:
        score += 40
    elif vocabulary_diversity > 0.6:
        score += 25
    else:
        score += 10

    return min(score, 100)