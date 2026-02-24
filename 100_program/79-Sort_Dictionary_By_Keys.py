# Sort dictionary by keys

data = eval(input("Enter dictionary: "))

sorted_dict = {}

for key in sorted(data.keys()):
    sorted_dict[key] = data[key]

print("Sorted by Keys:", sorted_dict)


# Output:
# Enter dictionary: {'b':2,'a':1,'c':3}
# Sorted by Keys: {'a': 1, 'b': 2, 'c': 3}
