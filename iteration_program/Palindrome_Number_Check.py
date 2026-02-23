# Program Name: Palindrome Number Check
# This program checks whether a number is palindrome or not

num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if reverse == num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# Output:
# Enter a number: 121
# Palindrome Number
