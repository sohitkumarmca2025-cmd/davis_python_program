# Count occurrence of element in tuple

numbers = tuple(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element to count: "))

count = 0
for num in numbers:
    if num == element:
        count += 1

print("Occurrence:", count)


# Output:
# Enter numbers: 1 2 2 3 2 4
# Enter element to count: 2
# Occurrence: 3
