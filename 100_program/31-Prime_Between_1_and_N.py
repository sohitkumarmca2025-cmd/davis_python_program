# Print all prime numbers between 1 and N

n = int(input("Enter N: "))

if n < 0:
    print("N invalid!")
else:
    for num in range(2, n + 1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)

# Output:
# Enter N: 10
# 2
# 3
# 5
# 7
