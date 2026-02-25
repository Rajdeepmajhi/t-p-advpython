import time

balance = 0.0
transactions = []

PASSWORD = "1234"
max_attempts = 3
lock_time = 30  

while True:
    attempts = 0

    
    while attempts < max_attempts:
        user_password = input("Enter password to access the Banking System: ")

        if user_password == PASSWORD:
            print("Access granted!\n")
            break
        else:
            attempts += 1
            print(f"Wrong password. Attempts left: {max_attempts - attempts}")

    
    if attempts == max_attempts:
        print(f"Too many wrong attempts. System locked for {lock_time} seconds...")
        time.sleep(lock_time)
        print("You can try again now.\n")
        continue

    
    while True:
        print("\nWelcome to the Banking System")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            transactions.append(f"Deposited: ${amount:.2f}")
            print(f"${amount:.2f} deposited successfully.")

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                transactions.append(f"Withdrew: ${amount:.2f}")
                print(f"${amount:.2f} withdrawn successfully.")

        elif choice == '3':
            print(f"Current Balance: ${balance:.2f}")

        elif choice == '4':
            print("Transaction History:")
            for t in transactions:
                print(t)

        elif choice == '5':
            print("Thank you for using the Banking System. Goodbye!")
            exit()

        else:
            print("Invalid choice. Please try again.")