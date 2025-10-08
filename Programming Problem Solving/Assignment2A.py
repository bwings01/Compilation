def atmmachine():
    balance = 0
    history = ""
    while True:
        print("[Welcome to Owl Banking]\nSelect an option:\n1 - Deposit\n2 - Withdrawal\n3 - Check balance\n4 - Check Transaction History\nQ - Quit")
        choice = input()
        if choice == "1":
            deposit = float(input("How much do you want to deposit: $"))
            previousbalance = balance
            balance += deposit
            history += f"${deposit:.2f} was deposited, balance went from ${previousbalance:.2f} to {balance:.2f} to ${balance:.2f}.\n"
        elif choice == "2":
            withdrawal = float(input("How much do you want to withdrawal: $"))
            if withdrawal > balance:
                print("Error: Cannot withdraw a larger amount than balance")
            elif withdrawal <= 0:
                print("Error: Cannot withdraw a smaller amount than balance")
            else:
                previousbalance = balance
                balance -= withdrawal
                history += f"${withdrawal:.2f} was withdrawn, balance went from ${previousbalance:.2f} to ${balance:.2f}.\n"
        elif choice == "3":
            print(f"Balance: ${balance:.2f}")
        elif choice == "4":
            print(history)
        elif choice == "Q":
            break
        else:
            print("Invalid Input!")
    return

if __name__ == "__main__":
    atmmachine()