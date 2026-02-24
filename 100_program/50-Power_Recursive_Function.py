# Calculate power using recursive function

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Result:", power(base, exp))


# Output:
# Enter base: 2
# Enter exponent: 3
# Result: 8
