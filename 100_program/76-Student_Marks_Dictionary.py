# Create student marks dictionary and find topper

n = int(input("Enter number of students: "))

students = {}

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

topper = max(students, key=students.get)

print("Topper:", topper)
print("Marks:", students[topper])


# Output:
# Enter number of students: 3
# Enter student name: A
# Enter marks: 80
# Enter student name: B
# Enter marks: 95
# Enter student name: C
# Enter marks: 85
# Topper: B
# Marks: 95
