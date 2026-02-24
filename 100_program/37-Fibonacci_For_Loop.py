# Generate Fibonacci series using for loop

n = int(input("Enter number of terms: "))

if n < 1:
    print("Number invalid!")
else:
    a, b = 0, 1

    for i in range(n):
        print(a)
        a, b = b, a + b

# Output:
# Enter number of terms: 5
# 0
# 1
# 1
# 2
# 3
