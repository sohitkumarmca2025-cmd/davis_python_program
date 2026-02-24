# Check whether one set is subset of another

set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

if set1.issubset(set2):
    print("Set1 is subset of Set2")
else:
    print("Set1 is not subset of Set2")


# Output:
# Enter first set: 1 2
# Enter second set: 1 2 3 4
# Set1 is subset of Set2
