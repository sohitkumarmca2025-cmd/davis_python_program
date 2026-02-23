# Program Name: Banking System
# This program performs deposit and withdrawal

balance = 10000   # Initial balance

print("1. Deposit")
print("2. Withdraw")

choice = int(input("Enter your choice: "))

if choice == 1:
    deposit = float(input("Enter deposit amount: "))
    balance = balance + deposit
    print("Updated Balance:", balance)

elif choice == 2:
    withdraw = float(input("Enter withdrawal amount: "))
    if withdraw <= balance:
        balance = balance - withdraw
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")
