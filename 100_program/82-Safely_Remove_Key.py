# Safely remove a key from dictionary

data = eval(input("Enter dictionary: "))
key = input("Enter key to remove: ")

if key in data:
    del data[key]
    print("Updated Dictionary:", data)
else:
    print("Key not found")


# Output:
# Enter dictionary: {'a':1,'b':2}
# Enter key to remove: a
# Updated Dictionary: {'b': 2}
