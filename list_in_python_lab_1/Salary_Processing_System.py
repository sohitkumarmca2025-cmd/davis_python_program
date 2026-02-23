# Program Name: Salary Processing System (Advanced)

salaries = [20000, 55000, 80000, 15000, 60000]

minimum_wage = 20000

# Remove below minimum wage
valid_salaries = [s for s in salaries if s >= minimum_wage]

# Add 5% bonus if salary > 50000
updated_salaries = []
for s in valid_salaries:
    if s > 50000:
        s *= 1.05
    updated_salaries.append(round(s,2))

updated_salaries.sort(reverse=True)

print("Sorted Salaries:", updated_salaries)
print("Top 3 Salaries:", updated_salaries[:3])

# Output:
# Sorted Salaries: [84000.0, 63000.0, 20000]
# Top 3 Salaries: [84000.0, 63000.0, 20000]
