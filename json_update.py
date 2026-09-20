import json

# Load existing file
with open("data/opinion.json", "r") as f:
    opinion = json.load(f)

# Add new information
opinion["restated_text"] = "Climate change poses serious risks"
opinion["faithfulness"] = "high"

# Save updated file
with open("data/opinion.json", "w") as f:
    json.dump(opinion, f, indent=4)

print("Updated!")
print(json.dumps(opinion, indent=4))
