# list for storing daily sales
totalSales = []

# main menu
def display_menu():
    print("[Owl Cafe]")
    while True:
        choice = int(input("1. Place ana Order\n2. View Daily Sales\n3. Exit\n> "))
        if choice == 1:
            take_order()
        elif choice == 2:
            show_sales()
        elif choice == 3:
            print("Thank you for visiting Owl Cafe!")
            break

# taking order
def take_order():
    # order total
    totalOrder = 0.0
    while True:
        orderSelection = int(input("1. Coffee - $3.50\n2. Sandwich - $5.75\n3. Smoothie - $4.25\n4. Muffin - $2.75\nSelect an item (1-4): "))
        try:
            if orderSelection == 1:
                item = "Coffee"
                price = 3.50 
            elif orderSelection == 2:
                item = "Sandwich"
                price = 5.75
            elif orderSelection == 3:
                item = "Smoothie"
                price = 4.25
            elif orderSelection == 4:
                item = "Muffin"
                price = 2.75
        except ValueError:
            print("Error: Please enter a number between 1 and 4.")
            continue

        # getting quantity
        try:
            quantity = int(input(f"Enter quantity of {item}: "))
        except ValueError:
            print("Error: Please enter a valid quantity.")
            continue

        # getting the total for each item added
        total = price * quantity
        totalOrder += total
        totalSales.append((item, quantity, total))
        print(f"Added {quantity} {item}(s) - ${total:.2f}")
        
        # if customer wants to add another item
        again = input("Add another item? (Y/N): ").strip().upper()
        if again != "Y":
            print(f"Order complete! Total for this order: ${totalOrder:.2f}\n")
            break

# daily sales
def show_sales():
    print(f"Today's Sales:")
    overall = 0.0
    # sales by item
    for item, total, quantity in totalSales:
        print(f"- {quantity} {item}(s): ${total:.2f}")
        # adding each total to the overall sales
        overall += total
    print(f"Total sales: ${overall:.2f}")


if __name__ == "__main__":
    display_menu()