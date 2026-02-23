# Program Name: Automorphic Number Check
# Automorphic Number: Square of number ends with same number

num = int(input("Enter a number: "))
square = num * num

if str(square).endswith(str(num)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

# Output:
# Enter a number: 25
# Automorphic Number
