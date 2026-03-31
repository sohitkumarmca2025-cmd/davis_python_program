# Input
numbers = [10, 20, 4, 45, 99]

# Process
if len(numbers) < 2:
    print("Error: Need at least two elements")
else:
    unique_numbers = list(set(numbers))
    first = second = float('-inf')

    for num in unique_numbers:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num

    # Output
    print("Second Largest Element:", second)
