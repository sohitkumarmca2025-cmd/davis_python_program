# File: exam_result.py

result = {
    "student": "Anjali",
    "marks": (60, 70, 80)
}

total = sum(result["marks"])
percentage = total / 3

print("Student:", result["student"])
print("Total:", total)
print("Percentage:", percentage)

# Output:
# Student: Anjali
# Total: 210
# Percentage: 70.0
