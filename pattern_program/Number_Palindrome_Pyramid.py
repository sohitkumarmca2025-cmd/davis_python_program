# Program Name: Number Palindrome Pyramid

rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    
    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    
    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    print()

# Output:
# Enter rows: 4
#    1
#   121
#  12321
# 1234321
