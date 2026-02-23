# Program Name: Class Division

percentage = float(input("Enter your percentage: "))

if percentage >= 75:
    division = "Distinction"
elif percentage >= 60:
    division = "First Division"
elif percentage >= 50:
    division = "Second Division"
elif percentage >= 40:
    division = "Third Division"
else:
    division = "Fail"

print("Division:", division)

# Output:
# Enter your percentage: 68
# Division: First Division
