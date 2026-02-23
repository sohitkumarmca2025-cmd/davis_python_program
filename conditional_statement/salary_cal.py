# Program Name: Salary Calculator

basic_salary = float(input("Enter Basic Salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10
gross_salary = basic_salary + hra + da

print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)

# Output:
# Enter Basic Salary: 20000
# HRA: 4000.0
# DA: 2000.0
# Gross Salary: 26000.0
