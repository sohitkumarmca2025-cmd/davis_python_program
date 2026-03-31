# Sort Tuples (Stable + Clean)

students = [("A", 50), ("B", 30), ("C", 40)]

sorted_students = sorted(students, key=lambda x: (x[1], x[0]))

print("Sorted List:", sorted_students)
