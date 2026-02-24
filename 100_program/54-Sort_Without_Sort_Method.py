# Sort list without using sort method (Bubble Sort)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted List:", numbers)


# Output:
# Enter numbers separated by space: 5 2 8 1
# Sorted List: [1, 2, 5, 8]
