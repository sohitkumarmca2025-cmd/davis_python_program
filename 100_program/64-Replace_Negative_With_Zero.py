# Replace negative numbers with zero

numbers = list(map(int, input("Enter numbers: ").split()))

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print("Updated List:", numbers)


# Output:
# Enter numbers: 5 -2 3 -7 8
# Updated List: [5, 0, 3, 0, 8]
