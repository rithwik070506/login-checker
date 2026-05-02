# Simple Login System

users = {
    "admin": "1234",
    "rithwik": "pass123"
}

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login Successful ✅")
    else:
        print("Invalid Username or Password ❌")

def signup():
    username = input("Create username: ")
    password = input("Create password: ")

    if username in users:
        print("Username already exists ❌")
    else:
        users[username] = password
        print("Signup Successful ✅")

while True:
    print("\n1. Login")
    print("2. Signup")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        login()
    elif choice == "2":
        signup()
    elif choice == "3":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice ❌")