# Calculate Compound Interest

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
if p < 0:
    print("Principal invalid!")
    
amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest:", ci)

# Output:
# Enter Principal: 1000
# Enter Rate: 10
# Enter Time: 2
# Compound Interest: 210.00
