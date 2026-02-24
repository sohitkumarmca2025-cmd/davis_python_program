# Reverse a number using while loop

num = int(input("Enter number: "))

if num < 0:
    print("Number invalid!")
else:
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    print("Reversed Number:", reverse)


# Output:
# Enter number: 1234
# Reversed Number: 4321
