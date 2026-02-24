# Find sum of digits

num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of Digits:", sum_digits)

# Output:
# Enter a number: 123
# Sum of Digits: 6
