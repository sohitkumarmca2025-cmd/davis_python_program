# Generate Fibonacci series using function

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

num = int(input("Enter number of terms: "))
if num < 0 :
    print("number of trum invalid !")
fibonacci(num)


# Output:
# Enter number of terms: 5
# 0
# 1
# 1
# 2
# 3
