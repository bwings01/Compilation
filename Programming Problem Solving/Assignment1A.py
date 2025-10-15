def receipt_generator():
    name = input("Enter your name: ")
    item = input("Enter the item you purchased: ")
    quantity = int(input("Enter the quantity: "))
    print(f"Thank you, {name}! You ordered {quantity} {item}(s).")
    return

if __name__ == '__main__':
    receipt_generator()