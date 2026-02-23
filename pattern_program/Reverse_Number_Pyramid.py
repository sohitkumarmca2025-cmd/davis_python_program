# Program Name: Reverse Number Pyramid

rows = int(input("Enter rows: "))

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Output:
# Enter rows: 4
# 4 3 2 1
#  3 2 1
#   2 1
#    1
