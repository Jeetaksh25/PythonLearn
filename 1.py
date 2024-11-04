balance = 0

while True:
    choice = int(input("Enter 1 to check balance, 2 to withdraw, 3 to deposit, and 4 to exit: "))
    
    if choice == 4:
        break
    elif choice == 1:
        print("Current balance:", balance)
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print("New balance:", balance)
    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("New balance:", balance)
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
