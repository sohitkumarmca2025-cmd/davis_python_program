# Program Name: Attendance Tracker (Advanced)

attendance = [1,0,1,1,0,0,1,1,1,0]

total_days = len(attendance)
present_days = attendance.count(1)
percentage = (present_days / total_days) * 100

# Identify below 75%
status = "Safe"
if percentage < 75:
    status = "Below 75% - Warning"

# Replace consecutive absences with flag
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "⚠"

print("Attendance %:", round(percentage,2))
print("Status:", status)
print("Updated Attendance:", attendance)

# Output:
# Attendance %: 60.0
# Status: Below 75% - Warning
# Updated Attendance: [1, 0, 1, 1, '⚠', 0, 1, 1, 1, 0]
