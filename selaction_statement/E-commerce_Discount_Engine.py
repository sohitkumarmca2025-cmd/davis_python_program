# Program Name: E-commerce Discount Engine
# This program calculates discount based on shopping amount

# Taking input from user
amount = float(input("Enter total purchase amount: "))

# Applying discount conditions
if amount >= 5000:
    discount = amount * 0.20   # 20% discount
elif amount >= 2000:
    discount = amount * 0.10   # 10% discount
else:
    discount = 0               # No discount

# Calculating final amount
final_amount = amount - discount

# Display result
print("Discount Amount:", discount)
print("Final Amount to Pay:", final_amount)
