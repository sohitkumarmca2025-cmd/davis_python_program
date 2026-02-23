# Program Name: Smart Login System
# This program checks username and password

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")

# Output:
# Enter username: admin
# Enter password: 1234
# Login Successful
