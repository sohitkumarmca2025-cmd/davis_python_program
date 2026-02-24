# Check whether key exists in dictionary

data = eval(input("Enter dictionary: "))
key = input("Enter key to check: ")

if key in data:
    print("Key exists")
else:
    print("Key does not exist")


# Output:
# Enter dictionary: {'a':1,'b':2}
# Enter key to check: b
# Key exists
