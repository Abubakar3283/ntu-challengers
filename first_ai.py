# Simple sentiment detection
# (is opinion positive or negative?)

opinions = [
    "I strongly believe climate change is dangerous",
    "Maybe pollution is somewhat concerning",
    "I am not sure about this topic",
    "This is definitely a serious problem"
]

# Simple rule-based detection (no API needed)
for opinion in opinions:
    if "strongly" in opinion or "definitely" in opinion:
        confidence = "HIGH"
    elif "maybe" in opinion or "not sure" in opinion:
        confidence = "LOW"
    else:
        confidence = "MEDIUM"
        
    if "dangerous" in opinion or "serious" in opinion:
        stance = "NEGATIVE about issue"
    else:
        stance = "NEUTRAL"
    
    print(f"Opinion: {opinion}")
    print(f"Confidence: {confidence}")
    print(f"Stance: {stance}")
    print("---")
