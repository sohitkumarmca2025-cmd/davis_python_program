# Merge two lists and remove duplicates

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

merged = list1 + list2

unique = []

for num in merged:
    if num not in unique:
        unique.append(num)

print("Merged Unique List:", unique)


# Output:
# Enter first list: 1 2 3
# Enter second list: 3 4 5
# Merged Unique List: [1, 2, 3, 4, 5]
