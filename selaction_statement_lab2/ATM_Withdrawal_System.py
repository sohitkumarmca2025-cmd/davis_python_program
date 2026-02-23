# Program Name: ATM Withdrawal System
# This program checks ATM withdrawal process

balance = 10000   # Available balance

amount = float(input("Enter withdrawal amount: "))

# Checking conditions
if amount <= balance:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")
