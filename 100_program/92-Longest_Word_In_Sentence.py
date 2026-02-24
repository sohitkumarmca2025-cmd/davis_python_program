# Find longest word in sentence

sentence = input("Enter sentence: ")

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)


# Output:
# Enter sentence: I love python programming
# Longest Word: programming
