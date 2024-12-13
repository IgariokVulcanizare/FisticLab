import json
from nltk.tokenize import word_tokenize
afinn = {}
with open('AFINN-111.txt', 'r', encoding='utf-8') as f:
    for line in f:
        word, score = line.strip().split('\t')
        afinn[word] = int(score)
def compute_tweet_score(text):
    tokens = word_tokenize(text.lower())
    score = sum(afinn.get(token, 0) for token in tokens)
    return score
with open('tweets.json', 'r', encoding='utf-8') as f:
    tweets = json.load(f)
scored_tweets = []
for tweet in tweets:
    tweet_id = tweet.get("id")
    text = tweet.get("text", "")
    score = compute_tweet_score(text)
    scored_tweets.append((tweet_id, text, score))
scored_tweets.sort(key=lambda x: x[2], reverse=True)
most_positive = scored_tweets[:10]
most_negative = scored_tweets[-10:]
print("10 Most Positive Tweets:")
for tweet_id, text, score in most_positive:
    print(f"ID: {tweet_id}, Score: {score}, Tweet: {text}")

print("\n10 Most Negative Tweets:")
for tweet_id, text, score in most_negative:
    print(f"ID: {tweet_id}, Score: {score}, Tweet: {text}")
