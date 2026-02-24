# Rotate a list by K positions (right rotation)

numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter K: "))

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k]

print("Rotated List:", rotated)


# Output:
# Enter numbers: 1 2 3 4 5
# Enter K: 2
# Rotated List: [4, 5, 1, 2, 3]
