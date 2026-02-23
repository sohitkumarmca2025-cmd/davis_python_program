# Program Name: Inventory Management

stock = [25, 0, 5, 12, 0, 8, 50]

# Remove items with 0 stock
stock = [s for s in stock if s > 0]

# Restock items below 10 (add 50 units)
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

# Calculate total inventory
total_inventory = sum(stock)

print("Updated Stock List:", stock)
print("Total Inventory Count:", total_inventory)

# Output:
# Updated Stock List: [25, 55, 12, 58, 50]
# Total Inventory Count: 200
