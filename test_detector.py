from detectors.llm_detector import detect_ai

text = input("Enter some text:\n")

score = detect_ai(text)

print(f"\nAI Score: {score}/100")