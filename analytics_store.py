import json
import os

ANALYTICS_FILE = "analytics.json"

def load_analytics():
    if not os.path.exists(ANALYTICS_FILE):
        return {
            "unique_pages": [],
            "word_counts": {},
            "longest_page": ["", 0],
            "subdomains": {}
            # "fingerprints": {},
            # "near_duplicates": []
        }
    with open(ANALYTICS_FILE, "r") as f:
        return json.load(f)

def save_analytics(data):
    with open(ANALYTICS_FILE, "w") as f:
        json.dump(data, f, indent=2)