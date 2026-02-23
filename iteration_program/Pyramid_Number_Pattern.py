# Program Name: Pyramid Number Pattern
# This program prints number pyramid pattern

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Output:
# Enter number of rows: 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4
