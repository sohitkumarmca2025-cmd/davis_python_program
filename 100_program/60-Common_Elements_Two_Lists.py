# Find common elements between two lists

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common Elements:", common)


# Output:
# Enter first list: 1 2 3 4
# Enter second list: 3 4 5 6
# Common Elements: [3, 4]
