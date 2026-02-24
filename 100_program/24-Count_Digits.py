# Count digits in a number

num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Total Digits:", count)

# Output:
# Enter number: 12345
# Total Digits: 5
