# File: Dictionary_Operations.py

# Creating dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

# Access value
print("Name:", student["name"])

# Add new key
student["marks"] = 85

# Update value
student["age"] = 21

# Delete key
del student["course"]

print("Updated Dictionary:", student)

# Output:
# Name: Rahul
# Updated Dictionary: {'name': 'Rahul', 'age': 21, 'marks': 85}
