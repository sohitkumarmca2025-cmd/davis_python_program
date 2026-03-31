def flatten(lst):
    return [item for sub in lst for item in (flatten(sub) if isinstance(sub, list) else [sub])]

nested = [1, [2, 3], [4, [5, 6]]]

print("Flattened List:", flatten(nested))

# Output:
# [1, 2, 3, 4, 5, 6]
