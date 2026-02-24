# Generate all substrings of a string

text = input("Enter string: ")

n = len(text)

for i in range(n):
    for j in range(i + 1, n + 1):
        print(text[i:j])


# Output:
# Enter string: abc
# a
# ab
# abc
# b
# bc
# c
