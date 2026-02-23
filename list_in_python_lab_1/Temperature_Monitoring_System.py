# Program Name: Temperature Monitoring System

temps = [38, 42, 45, 47, 39, 41, 44]

# Find hottest and coldest temperature
hottest = max(temps)
coldest = min(temps)

updated_temps = []
extreme_days = 0

for t in temps:
    if t > 45:
        updated_temps.append("Heat Alert")
    else:
        updated_temps.append(t)

    if t > 40:
        extreme_days += 1

print("Hottest Temperature:", hottest)
print("Coldest Temperature:", coldest)
print("Updated Temperature List:", updated_temps)
print("Extreme Days (>40°C):", extreme_days)

# Output:
# Hottest Temperature: 47
# Coldest Temperature: 38
# Updated Temperature List: [38, 42, 45, 'Heat Alert', 39, 41, 44]
# Extreme Days (>40°C): 5
