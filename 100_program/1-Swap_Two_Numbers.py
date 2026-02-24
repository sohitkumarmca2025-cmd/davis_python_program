# Swap two numbers without third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After Swapping:")
print("First Number:", a)
print("Second Number:", b)

# Output:
# Enter first number: 10
# Enter second number: 20
# After Swapping:
# First Number: 20
# Second Number: 10
