# Program Name: Income Tax Calculator
# This program calculates tax based on income

income = float(input("Enter your annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Total Tax to Pay:", tax)
