import json
from collections import Counter

ANALYTICS_FILE = "analytics.json"

def load_analytics():
    with open(ANALYTICS_FILE, "r") as f:
        return json.load(f)

def main():
    data = load_analytics()

    # -----------------------------
    # 1. Unique pages
    # -----------------------------
    unique_pages = set(data.get("unique_pages", []))
    print("=== Unique Pages ===")
    print(f"Total unique pages (fragment removed): {len(unique_pages)}\n")

    # -----------------------------
    # 2. Longest page
    # -----------------------------
    longest_url, longest_count = data.get("longest_page", ["", 0])
    print("=== Longest Page ===")
    print(f"URL: {longest_url}")
    print(f"Word count: {longest_count}\n")

    # -----------------------------
    # 3. Top 50 most common words
    # -----------------------------
    word_counts = data.get("word_counts", {})
    counter = Counter(word_counts)
    top_50 = counter.most_common(50)

    print("=== Top 50 Most Common Words ===")
    for word, freq in top_50:
        print(f"{word}: {freq}")
    print()

    # -----------------------------
    # 4. Subdomain counts
    # -----------------------------
    subdomains = data.get("subdomains", {})

    print("=== Subdomains Under *.uci.edu ===")
    print(f"Total subdomains: {len(subdomains)}\n")

    for subdomain in sorted(subdomains.keys()):
        print(f"{subdomain}, {subdomains[subdomain]}")

    print()

if __name__ == "__main__":
    main()