#list based transaction system
balance = 0
transaction = []
while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.CheckBalance")
    print("4.Transaction History")
    print("5.Exit")
    
    choice= int(input("Enter your choice:"))
    if choice == 1:
        amt = int(input("Enter Deposit Amount"))
        balance +=amt
        transaction.append("Deposited" + str(amt))
        print("Amount Deposited")
        
    elif choice == 2:
        amt = int(input("Enter Withdrawal Amount"))
        if amt <= balance:
            balance -=amt
            transaction.append("Withdrawl: " +str(amt))
            print("Amount Withdrawn")
           
        else:
            print("Insufficient Balance")
            
    elif choice == 3:
        print("Current Balance: ",balance)
        
    elif choice == 4:
        print("\nTransaction History") 
        if len(transaction) == 0:
            print("No Transaction Yet")
        else:
            for t in transaction:
                print(t) 
             
    elif choice == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
        