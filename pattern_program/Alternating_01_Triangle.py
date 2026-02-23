# Program Name: Alternating 0-1 Triangle

rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()

# Output:
# Enter rows: 4
# 0
# 1 0
# 0 1 0
# 1 0 1 0
