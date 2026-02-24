# Perform intersection of two sets

set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

intersection = set1 & set2

print("Intersection:", intersection)


# Output:
# Enter first set: 1 2 3 4
# Enter second set: 3 4 5 6
# Intersection: {3, 4}
