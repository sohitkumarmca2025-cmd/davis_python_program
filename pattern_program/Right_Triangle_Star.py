# Program Name: Right Triangle Star Pattern

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

# Output:
#    *
#   **
#  ***
# ****
