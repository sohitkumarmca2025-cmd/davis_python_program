# First Non-Repeating Character

text = "aabbcde"

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

result = next((ch for ch in text if freq[ch] == 1), None)

print("First Non-Repeating Character:", result)
