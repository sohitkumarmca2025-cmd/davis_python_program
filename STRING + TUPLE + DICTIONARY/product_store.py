# File: product_store.py

product = {
    "item": "Laptop",
    "price_details": (50000, 18)  # (price, GST %)
}

price = product["price_details"][0]
gst = price * product["price_details"][1] / 100
total = price + gst

print("Product:", product["item"])
print("Total Price:", total)

# Output:
# Product: Laptop
# Total Price: 59000.0
