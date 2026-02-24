# Replace all vowels with *

text = input("Enter string: ")

result = ""

for ch in text:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

print("Updated String:", result)


# Output:
# Enter string: hello
# Updated String: h*ll*
