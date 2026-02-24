# Print all divisors of a number

num = int(input("Enter number: "))

if num < 1:
    print("Number invalid!")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

# Output:
# Enter number: 6
# 1
# 2
# 3
# 6
