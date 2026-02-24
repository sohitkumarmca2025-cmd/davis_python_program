# Find GCD using while loop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD:", a)

# Output:
# Enter first number: 48
# Enter second number: 18
# GCD: 6
