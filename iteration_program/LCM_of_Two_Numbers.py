# Program Name: LCM of Two Numbers
# This program finds LCM using loop

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

max_num = max(num1, num2)

while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        print("LCM is:", max_num)
        break
    max_num += 1

# Output:
# Enter first number: 4
# Enter second number: 6
# LCM is: 12
