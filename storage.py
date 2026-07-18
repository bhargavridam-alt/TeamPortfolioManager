import json
import os

FILE_NAME = "members.json"


def load_members():
    """Load members from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_members(members):
    """Save members to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(members, file, indent=4)
