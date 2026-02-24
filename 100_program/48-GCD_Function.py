# Find GCD using function

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD:", gcd(x, y))

# Output:
# Enter first number: 48
# Enter second number: 18
# GCD: 6
