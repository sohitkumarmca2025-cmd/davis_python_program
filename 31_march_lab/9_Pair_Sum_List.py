numbers = [1, 2, 3, 4, 5]
target = 5

pairs = [(a, b) for i, a in enumerate(numbers) 
         for b in numbers[i+1:] if a + b == target]

print("Pairs:", pairs)

# Output:
# [(1, 4), (2, 3)]
