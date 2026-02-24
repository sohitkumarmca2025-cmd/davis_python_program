# Find smallest element in list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest Element:", smallest)


# Output:
# Enter numbers separated by space: 10 25 15 5
# Smallest Element: 5
