import json

# Load from file
with open("data/opinion.json", "r") as f:
    loaded = json.load(f)

print("User:", loaded["user"])
print("Their opinion:", loaded["original_text"])
print("Emotion:", loaded["emotion"])
