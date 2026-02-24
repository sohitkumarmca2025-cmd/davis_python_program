# Find sum of first N natural numbers

n = int(input("Enter Number: "))

if n < 1:
    print("Number invalid!")
else:
    total = 0
    for i in range(1, n + 1):
        total += i

    print("Sum:", total)

# Output:
# Enter Number: 5
# Sum: 15
