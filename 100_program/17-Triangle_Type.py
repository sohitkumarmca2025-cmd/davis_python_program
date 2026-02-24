# Determine Type of Triangle using Angles

angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

# Check valid triangle
if angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180:

    if angle1 == angle2 == angle3:
        print("Equilateral Triangle")

    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("Not a Valid Triangle")

# Output:
# Enter angle 1: 60
# Enter angle 2: 60
# Enter angle 3: 60
# Equilateral Triangle
