# Program Name: Time Converter

seconds = int(input("Enter time in seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)

# Output:
# Enter time in seconds: 3665
# Hours: 1
# Minutes: 1
# Seconds: 5
