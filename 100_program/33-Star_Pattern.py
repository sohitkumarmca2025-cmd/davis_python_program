# Print star pattern using for loop

n = int(input("Enter number of rows: "))
if n<1 :
    print(" enter row invalide !")
    
for i in range(1, n + 1):
    print("*" * i)

# Output:
# Enter number of rows: 4
# *
# **
# ***
# ****
