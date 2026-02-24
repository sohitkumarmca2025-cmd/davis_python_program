# Count uppercase and lowercase letters

text = input("Enter string: ")

upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)


# Output:
# Enter string: HelloWorld
# Uppercase Letters: 2
# Lowercase Letters: 8
