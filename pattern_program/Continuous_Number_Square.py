# Program Name: Continuous Number Square

n = int(input("Enter size: "))
num = 1

for i in range(n):
    for j in range(n):
        print(num, end=" ")
        num += 1
    print()

# Output:
# Enter size: 3
# 1 2 3
# 4 5 6
# 7 8 9
