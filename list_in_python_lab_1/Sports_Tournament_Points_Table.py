# Program Name: Sports Tournament Points Table

points = [15, 22, -5, 18, 30, 12]

# Replace negative points with 0
points = [p if p >= 0 else 0 for p in points]

# Sort leaderboard in descending order
points.sort(reverse=True)

winner = points[0]
runner_up = points[1]

print("Sorted Leaderboard:", points)
print("Winner Points:", winner)
print("Runner-Up Points:", runner_up)

# Output:
# Sorted Leaderboard: [30, 22, 18, 15, 12, 0]
# Winner Points: 30
# Runner-Up Points: 22
