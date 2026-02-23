# File: city_temperature.py

city = {
    "name": "Delhi",
    "temp": (30, 35, 40)  # Morning, Afternoon, Evening
}

avg_temp = sum(city["temp"]) / len(city["temp"])

print("City:", city["name"])
print("Temperatures:", city["temp"])
print("Average Temperature:", avg_temp)

# Output:
# City: Delhi
# Temperatures: (30, 35, 40)
# Average Temperature: 35.0
