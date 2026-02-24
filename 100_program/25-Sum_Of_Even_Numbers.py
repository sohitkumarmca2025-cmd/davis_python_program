# Find sum of even numbers up to N

n = int(input("Enter N: "))
i = 1
total = 0

while i <= n:
    if i % 2 == 0:
        total += i
    i += 1

print("Sum of Even Numbers:", total)

# Output:
# Enter N: 10
# Sum of Even Numbers: 30
