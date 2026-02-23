# File: employee_data.py

employee = {
    "id": 101,
    "name": "Amit",
    "salary": (25000, 3000)  # (basic, bonus)
}

total_salary = sum(employee["salary"])

print(f"Employee Name: {employee['name']}")
print("Salary Details:", employee["salary"])
print("Total Salary:", total_salary)

# Output:
# Employee Name: Amit
# Salary Details: (25000, 3000)
# Total Salary: 28000
