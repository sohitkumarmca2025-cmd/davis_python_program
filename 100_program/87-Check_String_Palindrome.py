# Check whether string is palindrome

text = input("Enter string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# Output:
# Enter string: madam
# Palindrome
