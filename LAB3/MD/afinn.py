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
with open('results.txt', 'w', encoding='utf-8') as out:
    for tweet in tweets:
        tweet_id = tweet.get("id")
        text = tweet.get("text", "")
        score = compute_tweet_score(text)
        out.write(f"{tweet_id}\t{score}\n")

print("Emotional values have been computed and stored in results.txt.")
