# Perform union of two sets

set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

union = set1 | set2

print("Union:", union)


# Output:
# Enter first set: 1 2 3
# Enter second set: 3 4 5
# Union: {1, 2, 3, 4, 5}
