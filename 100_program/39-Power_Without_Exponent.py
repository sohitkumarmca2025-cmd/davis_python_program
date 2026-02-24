# Calculate power without using exponent operator

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1

for i in range(exp):
    result *= base

print("Result:", result)

# Output:
# Enter base: 2
# Enter exponent: 3
# Result: 8
