# Program Name: Student Marks Analyzer

marks = [95, 102, 76, -5, 88, 67, 45, 110, 76]

# Remove invalid marks
valid_marks = [m for m in marks if 0 <= m <= 100]

# Calculate average
average = sum(valid_marks) / len(valid_marks)

# Find topper(s)
top_score = max(valid_marks)
toppers = [m for m in valid_marks if m == top_score]

# Grade based on average
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
else:
    grade = "C"

print("Valid Marks:", valid_marks)
print("Average:", average)
print("Topper Score:", toppers)
print("Grade:", grade)

# Output:
# Valid Marks: [95, 76, 88, 67, 45, 76]
# Average: 74.5
# Topper Score: [95]
# Grade: B
