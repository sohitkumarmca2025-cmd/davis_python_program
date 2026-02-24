# Count frequency of elements in list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)


# Output:
# Enter numbers separated by space: 1 2 2 3 3 3
# Frequency: {1: 1, 2: 2, 3: 3}
