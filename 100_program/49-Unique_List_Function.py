# Return unique elements from list using function

def unique_elements(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique


numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Unique Elements:", unique_elements(numbers))


# Output:
# Enter numbers separated by space: 1 2 2 3 4 4
# Unique Elements: [1, 2, 3, 4]
