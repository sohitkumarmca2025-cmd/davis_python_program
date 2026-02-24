# Calculate Simple Interest with validation

p = float(input("Enter Principal: "))

if p < 0:
    print("Principal invalid!")
else:
    r = float(input("Enter Rate: "))
    t = float(input("Enter Time in year: "))

    si = (p * r * t) / 100

    print("Simple Interest:", si)


# Output:
# Enter Principal: 1000
# Enter Rate: 5
# Enter Time in year: 2
# Simple Interest: 100.0
