data = {"a": 1, "b": 2, "c": 3}

swapped = {v: k for k, v in data.items()}

print("Swapped Dictionary:", swapped)

# Output:
# {1: 'a', 2: 'b', 3: 'c'}
