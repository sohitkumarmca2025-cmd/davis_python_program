# File: login_system.py

users = {
    "admin": ("admin123", "active"),
    "user": ("user123", "inactive")
}

username = "admin"
password = "admin123"

if username in users and users[username][0] == password:
    print("Login Successful")
else:
    print("Login Failed")

# Output:
# Login Successful
