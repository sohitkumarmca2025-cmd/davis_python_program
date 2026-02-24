# Find key with maximum value

data = eval(input("Enter dictionary: "))

max_key = max(data, key=data.get)

print("Key with Maximum Value:", max_key)
print("Maximum Value:", data[max_key])


# Output:
# Enter dictionary: {'a':10,'b':25,'c':15}
# Key with Maximum Value: b
# Maximum Value: 25
