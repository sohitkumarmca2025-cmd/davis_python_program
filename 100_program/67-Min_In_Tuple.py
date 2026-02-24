# Find minimum value in a tuple

numbers = tuple(map(int, input("Enter numbers: ").split()))

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum in Tuple:", minimum)


# Output:
# Enter numbers: 10 25 5 40
# Minimum in Tuple: 5
