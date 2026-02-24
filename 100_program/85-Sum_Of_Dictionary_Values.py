# Find sum of all dictionary values

data = eval(input("Enter dictionary: "))

total = 0

for value in data.values():
    total += value

print("Sum of Values:", total)


# Output:
# Enter dictionary: {'a':10,'b':20,'c':30}
# Sum of Values: 60
