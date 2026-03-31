import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar"]
revenue = [100,200,150]

plt.plot(months, revenue)
plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.grid()

plt.show()

# Output:
# Styled graph displayed
