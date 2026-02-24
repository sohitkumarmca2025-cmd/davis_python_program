# Convert string to title case manually

text = input("Enter sentence: ")

result = ""
new_word = True

for ch in text:
    if ch == " ":
        result += ch
        new_word = True
    else:
        if new_word:
            result += ch.upper()
            new_word = False
        else:
            result += ch.lower()

print("Title Case:", result)


# Output:
# Enter sentence: hello world
# Title Case: Hello World
