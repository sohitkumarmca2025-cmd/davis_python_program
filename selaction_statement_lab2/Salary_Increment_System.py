# Program Name: Salary Increment System
# This program calculates salary increment based on performance rating

salary = float(input("Enter current salary: "))
rating = int(input("Enter performance rating (1-5): "))

if rating == 5:
    increment = salary * 0.20
elif rating >= 3:
    increment = salary * 0.10
else:
    increment = salary * 0.05

new_salary = salary + increment

print("Increment Amount:", increment)
print("New Salary:", new_salary)

# Output:
# Enter current salary: 50000
# Enter performance rating (1-5): 4
# Increment Amount: 5000.0
# New Salary: 55000.0
