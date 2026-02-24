# Assign grades based on marks

marks = int(input("Enter marks: "))
if marks > 100 :
    print("markes invalid !")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Output:
# Enter marks: 82
# Grade B
