# Program Name: Strong Number Check
# This program checks whether a number is Strong Number or not
# Strong Number: Sum of factorial of digits = number

num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    
    # Finding factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    
    sum += fact
    temp //= 10

if sum == num:
    print("Strong Number")
else:
    print("Not a Strong Number")

# Output:
# Enter a number: 145
# Strong Number
