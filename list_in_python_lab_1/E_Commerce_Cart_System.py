# Program Name: E-Commerce Cart System 

cart = [2000, 1500, 2000, 800, 1200]

# Remove duplicates
cart = list(set(cart))

subtotal = sum(cart)

discount = 0
if subtotal > 5000:
    discount = subtotal * 0.10

after_discount = subtotal - discount

gst = after_discount * 0.18
final_amount = after_discount + gst

print("Unique Items:", cart)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("GST (18%):", round(gst,2))
print("Final Payable Amount:", round(final_amount,2))

# Output:
# Unique Items: [2000, 1500, 800, 1200]
# Subtotal: 5500
# Discount: 550.0
# GST (18%): 891.0
# Final Payable Amount: 5841.0
