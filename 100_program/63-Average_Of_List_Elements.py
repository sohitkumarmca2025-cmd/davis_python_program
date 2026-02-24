# Find average of list elements

numbers = list(map(int, input("Enter numbers: ").split()))

total = 0
for num in numbers:
    total += num

average = total / len(numbers)

print("Average:", average)


# Output:
# Enter numbers: 2 4 6 8
# Average: 5.0
