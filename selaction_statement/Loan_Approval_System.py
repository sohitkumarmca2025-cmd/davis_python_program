# Program Name: Loan Approval System
# This program checks loan eligibility

salary = float(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score: "))

# Checking condition
if salary >= 30000 and credit_score >= 700:
    print("Loan Approved")
else:
    print("Loan Rejected")
