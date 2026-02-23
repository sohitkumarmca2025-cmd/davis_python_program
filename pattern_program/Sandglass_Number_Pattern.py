# Program Name: Sandglass Number Pattern

rows = int(input("Enter rows: "))

# Upper part
for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Lower part
for i in range(2, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Output:
# Enter rows: 3
# 1 2 3
#  1 2
#   1
#  1 2
# 1 2 3
