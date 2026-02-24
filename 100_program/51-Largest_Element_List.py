# Find largest element in list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest Element:", largest)


# Output:
# Enter numbers separated by space: 10 25 15 40
# Largest Element: 40
