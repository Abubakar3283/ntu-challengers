import json

opinion = {
    "user": "Abu Bakar",
    "original_text": "I feel climate change is bad",
    "stance": "negative",
    "emotion": "worried"
}

# Save to file
with open("data/opinion.json", "w") as f:
    json.dump(opinion, f, indent=4)

print("Saved successfully!")
