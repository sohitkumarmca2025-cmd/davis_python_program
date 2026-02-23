# Program Name: Electricity Bill Calculator
# This program calculates electricity bill based on units consumed

units = int(input("Enter electricity units consumed: "))

# Applying slab rates
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

print("Total Electricity Bill:", bill)

# output
#Enter electricity units consumed: 150
#Total Electricity Bill: 1050
