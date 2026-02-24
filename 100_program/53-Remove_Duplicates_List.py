# Remove duplicate elements from list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)


# Output:
# Enter numbers separated by space: 1 2 2 3 4 4
# List without duplicates: [1, 2, 3, 4]
