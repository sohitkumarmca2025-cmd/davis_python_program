# File: student_record.py

# Dictionary storing student data
student = {
    "name": "Rahul",
    "marks": (78, 85, 90)   # Tuple of marks
}

# Calculate total
total = sum(student["marks"])

# Print formatted string
print("Student Name:", student["name"])
print("Marks:", student["marks"])
print("Total Marks:", total)

# Output:
# Student Name: Rahul
# Marks: (78, 85, 90)
# Total Marks: 253
