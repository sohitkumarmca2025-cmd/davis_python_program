# Program Name: Perfect Number Check
# This program checks whether a number is perfect or not

num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# Output:
# Enter a number: 6
# Perfect Number
