# Find second largest number in list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

# Sort manually
for i in range(len(unique)):
    for j in range(0, len(unique) - i - 1):
        if unique[j] > unique[j + 1]:
            unique[j], unique[j + 1] = unique[j + 1], unique[j]

print("Second Largest:", unique[-2])


# Output:
# Enter numbers separated by space: 10 25 15 40
# Second Largest: 25
