# Check whether tuple elements are unique

numbers = tuple(map(int, input("Enter numbers: ").split()))

unique = True

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            unique = False

if unique:
    print("All elements are unique")
else:
    print("Duplicate elements found")


# Output:
# Enter numbers: 1 2 3 4
# All elements are unique
