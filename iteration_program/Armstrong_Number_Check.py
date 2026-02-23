# Program Name: Armstrong Number Check
# This program checks whether a number is Armstrong or not

num = int(input("Enter a number: "))
temp = num
sum = 0

# Counting number of digits
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Output:
# Enter a number: 153
# Armstrong Number
