# Program Name: Prime Numbers in Range
# This program prints prime numbers between two numbers

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# Output:
# Enter start number: 10
# Enter end number: 20
# 11
# 13
# 17
# 19
