# Program Name: Hospital Emergency Triage
# This program decides patient priority

condition = input("Enter patient condition (critical/serious/normal): ")

if condition.lower() == "critical":
    print("Immediate Treatment Required")
elif condition.lower() == "serious":
    print("Treat After Critical Patients")
else:
    print("Normal Queue")

# Output:
# Enter patient condition (critical/serious/normal): critical
# Immediate Treatment Required
