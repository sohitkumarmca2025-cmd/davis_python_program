# File: bank_account.py

account = {
    "holder": "Ramesh",
    "transactions": (5000, -2000, 3000)
}

balance = sum(account["transactions"])

print("Account Holder:", account["holder"])
print("Final Balance:", balance)

# Output:
# Account Holder: Ramesh
# Final Balance: 6000
