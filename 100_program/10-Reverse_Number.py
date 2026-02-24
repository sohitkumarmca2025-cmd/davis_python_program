# Reverse a number

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number:", reverse)

# Output:
# Enter a number: 1234
# Reversed Number: 4321
