# Create dictionary from two lists

keys = input("Enter keys separated by space: ").split()
values = list(map(int, input("Enter values separated by space: ").split()))

dictionary = {}

for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print("Created Dictionary:", dictionary)


# Output:
# Enter keys separated by space: a b c
# Enter values separated by space: 10 20 30
# Created Dictionary: {'a': 10, 'b': 20, 'c': 30}
