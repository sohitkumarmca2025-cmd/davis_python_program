# Program Name: Hollow Diamond Advanced Pattern

rows = int(input("Enter rows: "))

# Upper part
for i in range(1, rows + 1):
    for j in range(1, 2*rows):
        if j == rows - i + 1 or j == rows + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part
for i in range(rows - 1, 0, -1):
    for j in range(1, 2*rows):
        if j == rows - i + 1 or j == rows + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Output:
# Enter rows: 3
#   *
#  * *
# *   *
#  * *
#   *
