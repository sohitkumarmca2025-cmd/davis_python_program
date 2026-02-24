# Perform difference of two sets

set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

difference = set1 - set2

print("Difference (Set1 - Set2):", difference)


# Output:
# Enter first set: 1 2 3 4
# Enter second set: 3 4 5
# Difference (Set1 - Set2): {1, 2}
