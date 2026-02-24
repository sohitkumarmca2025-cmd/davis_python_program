# Find sum of digits using function

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


num = int(input("Enter number: "))

if num < 0:
    print("Number invalid!")
else:
    print("Sum of Digits:", sum_digits(num))

# Output:
# Enter number: 123
# Sum of Digits: 6
