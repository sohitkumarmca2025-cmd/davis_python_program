# Find factorial using function

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter number: "))
if num < 0:
    print("number invalid !")
else:    
    print("Factorial:", factorial(num))

# Output:
# Enter number: 5
# Factorial: 120
