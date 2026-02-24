# Count vowels in a string

text = input("Enter a string: ")

count = 0
for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Total Vowels:", count)

# Output:
# Enter a string: hello
# Total Vowels: 2
