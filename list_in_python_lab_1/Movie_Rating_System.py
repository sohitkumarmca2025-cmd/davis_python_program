# Program Name: Movie Rating System

ratings = [5, 4, 3, 6, 2, 5, -1, 4]

# Remove invalid ratings (1–5 only)
valid_ratings = [r for r in ratings if 1 <= r <= 5]

# Calculate average rating
average_rating = sum(valid_ratings) / len(valid_ratings)

# Count 5-star ratings
five_star_count = valid_ratings.count(5)

# Sort ratings in ascending order
valid_ratings.sort()

print("Valid Ratings:", valid_ratings)
print("Average Rating:", round(average_rating, 2))
print("5-Star Ratings:", five_star_count)

# Output:
# Valid Ratings: [2, 3, 4, 4, 5, 5]
# Average Rating: 3.83
# 5-Star Ratings: 2
