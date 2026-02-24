# Find first non-repeating character

text = input("Enter string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First Non-Repeating Character:", ch)
        break


# Output:
# Enter string: swiss
# First Non-Repeating Character: w
