# Find maximum value in a tuple

numbers = tuple(map(int, input("Enter numbers: ").split()))

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum in Tuple:", maximum)


# Output:
# Enter numbers: 10 25 15 40
# Maximum in Tuple: 40
