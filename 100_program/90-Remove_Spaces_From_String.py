# Remove spaces from string

text = input("Enter string: ")

result = ""

for ch in text:
    if ch != " ":
        result += ch

print("String without spaces:", result)


# Output:
# Enter string: hello world
# String without spaces: helloworld
