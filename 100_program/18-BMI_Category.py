# Calculate BMI category

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (meter): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# Output:
# Enter weight (kg): 70
# Enter height (meter): 1.75
# Normal
