# Program Name: Shopping Bill Calculator

total = float(input("Enter total shopping amount: "))

discount = 0
if total > 5000:
    discount = total * 0.10

final_amount = total - discount

print("Discount:", discount)
print("Final Amount to Pay:", final_amount)

# Output:
# Enter total shopping amount: 6000
# Discount: 600.0
# Final Amount to Pay: 5400.0
