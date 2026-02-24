# Remove duplicate characters from string

text = input("Enter string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("Without Duplicates:", result)


# Output:
# Enter string: programming
# Without Duplicates: progamin
