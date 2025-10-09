def printMenu():
    print("[Owl About Coffee]")
    print("1. Espresso      - $3.00")
    print("2. Latte         - $4.00")
    print("3. Cappuccino    - $4.00")
    print("4. Tea           - $2.00")
    print("5. Exit and Checkout")


def getChoice():
    try:
        choice = int(input("> "))
        if choice in [1, 2, 3, 4, 5]:
            return choice
        else:
            return -1
    except ValueError:
        return -1


def processOrder(choice):
    prices = {1: 3.00, 2: 4.00, 3: 4.00, 4: 2.00}
    items = {1: "Espresso", 2: "Latte", 3: "Cappuccino", 4: "Tea"}
    try:
        amount = int(input(f"How Many {items[choice]}(s) would you like?"))
        total = prices[choice] * amount
        return total
    except ValueError:
        print("Invalid amount entered.")

def getTotal(subtotal):
    if subtotal > 0:
        tax = .06 * subtotal
        total = subtotal + tax
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax (6%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")
    else:
        print("No items ordered")

def main():
    subtotal = 0
    while True:
        printMenu()
        choice = getChoice()
        if choice == -1:
            print("Invalid choice")
            continue
        elif choice == 5:
            getTotal(subtotal)
            break
        else:
            subtotal += processOrder(choice)

if __name__ == "__main__":
    main()