# Reverse a string without slicing

text = input("Enter string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed String:", reverse)


# Output:
# Enter string: hello
# Reversed String: olleh
