# Validate username and password

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

# Output:
# Enter username: admin
# Enter password: 1234
# Login Successful
