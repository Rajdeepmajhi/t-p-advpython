'''6. Write a program:
 - Simulate login system
 - Use file to store username/password'''

# File name
filename = "users.txt"

# Function to register user
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(filename, "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration successful!\n")

# Function to login
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open(filename, "r") as file:
            users = file.readlines()

        for user in users:
            u, p = user.strip().split(",")
            if u == username and p == password:
                print("Login successful!")
                return
        
        print("Invalid username or password")

    except FileNotFoundError:
        print("No users registered yet!")

# Menu
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice")