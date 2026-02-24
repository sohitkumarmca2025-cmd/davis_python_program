# Count vowels using function

def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count

text = input("Enter string: ")
print("Total Vowels:", count_vowels(text))

# Output:
# Enter string: hello
# Total Vowels: 2
