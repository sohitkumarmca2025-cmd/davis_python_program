# Program Name: Online Exam Result Processor (Advanced)

scores = [25, 34, 40, 55, 30, 80, 20]

# Remove lowest 2 scores
scores = sorted(scores)[2:]

# Add grace marks (30–35)
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

passed_students = len([s for s in scores if s >= 40])

print("Updated Scores:", scores)
print("Passed Students:", passed_students)

# Output:
# Updated Scores: [30, 40, 55, 35, 80]
# Passed Students: 3
