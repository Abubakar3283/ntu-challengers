import json

# Create a user opinion in JSON format
user_opinion = {
    "name": "Abu Bakar",
    "topic": "Climate Change",
    "stance": "I think it is a serious problem",
    "confidence": "high",
    "emotion": "concerned"
}

# Print it nicely
print(json.dumps(user_opinion, indent=4))
