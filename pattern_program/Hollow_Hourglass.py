# Program Name: Hollow Hourglass Pattern

rows = int(input("Enter rows: "))

# Upper part
for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(1, 2*i):
        if j == 1 or j == 2*i - 1 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part
for i in range(2, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, 2*i):
        if j == 1 or j == 2*i - 1 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Output:
# Enter rows: 3
# *****
#  * *
#   *
#  * *
# *****
