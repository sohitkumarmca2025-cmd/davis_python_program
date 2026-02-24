# Reverse a string using for loop

text = input("Enter a string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed String:", reverse)

# Output:
# Enter a string: hello
# Reversed String: olleh
