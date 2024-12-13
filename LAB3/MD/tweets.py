import json
import re
from collections import Counter

filename = "tweets.json"
hashtag_pattern = re.compile(r"#(\w+)")
hashtag_counts = Counter()

with open(filename, 'r', encoding='utf-8') as f:
    data = json.load(f)

for tweet in data:
    text = tweet.get("text", "")
    hashtags = hashtag_pattern.findall(text)
    for h in hashtags:
        hashtag_counts[h.lower()] += 1

top_10 = hashtag_counts.most_common(10)

for hashtag, count in top_10:
    print(f"#{hashtag}: {count}")
