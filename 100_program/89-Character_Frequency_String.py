# Find frequency of each character in string

text = input("Enter string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:", frequency)


# Output:
# Enter string: hello
# Character Frequency: {'h':1,'e':1,'l':2,'o':1}
