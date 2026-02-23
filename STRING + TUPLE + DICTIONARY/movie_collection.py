# File: movie_collection.py

movie = {
    "title": "KGF",
    "ratings": (4, 5, 5, 4)
}

avg_rating = sum(movie["ratings"]) / len(movie["ratings"])

print("Movie:", movie["title"])
print("Average Rating:", avg_rating)

# Output:
# Movie: KGF
# Average Rating: 4.5
