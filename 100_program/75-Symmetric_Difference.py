# Find symmetric difference of two sets

set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

sym_diff = set1 ^ set2

print("Symmetric Difference:", sym_diff)


# Output:
# Enter first set: 1 2 3
# Enter second set: 3 4 5
# Symmetric Difference: {1, 2, 4, 5}
