tran_his = []
balance = 10000
pin = 9583

def Deposite_amount():
    global balance
    amt = int(input("Enter amount to deposit: "))
    old_balance = balance
    balance = balance + amt

    print("\n--- Deposit Details ---")
    print("Old Balance :", old_balance)
    print("Deposit Amt :", amt)
    print("New Balance :", balance)

    tran_his.append(f"Deposit: {old_balance} + {amt} = {balance}")

def Withdraw_amount():
    global balance
    amt = int(input("Enter amount to withdraw: "))

    if amt > balance:
        print(" Insufficient balance")
    else:
        old_balance = balance
        balance = balance - amt

        print("\n--- Withdraw Details ---")
        print("Old Balance :", old_balance)
        print("Withdraw Amt:", amt)
        print("New Balance :", balance)

        tran_his.append(f"Withdraw: {old_balance} - {amt} = {balance}")

def Check_the_balance():
    print("\nCurrent Balance =", balance)

def Show_transaction_history():
    print("\Transaction History:")
    if len(tran_his) == 0:
        print("No transactions yet.")
    else:
        for i in tran_his:
            print(" ", i)

print("Welcome to AXIC BANK")

attempt = 0
while attempt < 3:
    ent_pin = int(input("Enter your PIN: "))

    if ent_pin == pin:
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                Deposite_amount()
            elif choice == "2":
                Withdraw_amount()
            elif choice == "3":
                Check_the_balance()
            elif choice == "4":
                Show_transaction_history()
            elif choice == "5":
                print("Thank you for using AXIC BANK")
                break
            else:
                print("Invalid choice")

        break
    else:
        print("Wrong PIN")
        attempt += 1
