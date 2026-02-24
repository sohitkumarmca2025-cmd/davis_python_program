# Check whether list is palindrome

numbers = list(map(int, input("Enter numbers: ").split()))

if numbers == numbers[::-1]:
    print("Palindrome List")
else:
    print("Not Palindrome")


# Output:
# Enter numbers: 1 2 3 2 1
# Palindrome List
