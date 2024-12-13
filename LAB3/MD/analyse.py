title = "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats."

categories = {
    "Dinosaurs": ["t-rex", "dinosaur", "prehistoric"],
    "Science Fiction": ["multi universes", "multiverse", "parallel universe", "sci-fi"],
    "Technology/Internet": ["internet", "web", "online", "digital"],
    "Politics": ["politics", "government", "election"],
    "Art": ["art", "artists", "paintings"],
    "Animals": ["cats", "dogs", "birds", "animals"]
}

lower_title = title.lower()

matched_categories = set()
for category, keywords in categories.items():
    for keyword in keywords:
        if keyword in lower_title:
            matched_categories.add(category)
            break

for cat in sorted(matched_categories):
    print("-", cat)
