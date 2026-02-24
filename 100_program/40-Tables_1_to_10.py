# Print multiplication tables from 1 to 10

for num in range(1, 11):
    print("\nTable of", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

# Output:
# Table of 1
# 1 x 1 = 1
# ...
# 10 x 10 = 100
