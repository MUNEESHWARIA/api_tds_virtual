import requests
import json
import time
from datetime import datetime

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY_ID = 67  # Replace with the correct TDS category ID if needed
HEADERS = {"User-Agent": "TDS Virtual TA Bot"}

def get_topics():
    all_topics = []
    page = 0

    while True:
        url = f"{BASE_URL}/c/tools-in-data-science/{CATEGORY_ID}.json?page={page}"
        print(f"Fetching: {url}")
        res = requests.get(url, headers=HEADERS)

        if res.status_code != 200:
            break

        topics = res.json().get("topic_list", {}).get("topics", [])
        if not topics:
            break

        all_topics.extend(topics)
        page += 1
        time.sleep(1)  # Be respectful to the server

    return all_topics

def filter_by_date(topics, start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    filtered = []
    for topic in topics:
        created_at = datetime.strptime(topic["created_at"][:10], "%Y-%m-%d")
        if start <= created_at <= end:
            filtered.append(topic)
    return filtered

def save_json(data, filename="tds_discourse_posts.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    topics = get_topics()
    print(f"Total topics fetched: {len(topics)}")
    
    filtered = filter_by_date(topics, "2025-01-01", "2025-04-14")
    print(f"Topics after date filtering: {len(filtered)}")

    save_json(filtered)
