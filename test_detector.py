from detectors.llm_detector import detect_ai
from detectors.stylometry import analyze_style
from detectors.confidence import calculate_confidence

text = input("Enter some text:\n")

llm_score = detect_ai(text)
style_score = analyze_style(text)

result = calculate_confidence(llm_score, style_score)

print(f"\nLLM Score: {llm_score}/100")
print(f"Stylometry Score: {style_score}/100")
print(f"Confidence: {result['confidence']}/100")
print(f"Label: {result['label']}")