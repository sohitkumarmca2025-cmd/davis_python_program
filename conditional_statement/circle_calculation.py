# Program Name: Circle Calculation

import math

radius = float(input("Enter radius of circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Area of Circle:", round(area,2))
print("Circumference of Circle:", round(circumference,2))

# Output:
# Enter radius of circle: 7
# Area of Circle: 153.94
# Circumference of Circle: 43.98
