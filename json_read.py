import json

# Reading data from JSON
user_opinion = {
    "name": "Abu Bakar",
    "stance": "Climate change is serious",
    "points": ["pollution", "flooding", "heat"]
}

# Read one specific thing
print("Name:", user_opinion["name"])
print("Stance:", user_opinion["stance"])
print("First point:", user_opinion["points"][0])
