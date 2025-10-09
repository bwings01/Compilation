def validate(message, offset):
    if offset < 0 or offset > 26:
        return False
    for char in message:
        if not (char.isalpha() or char.isspace()):
            return False
    return True
    
def encrypt(message, offset):
    message = message.upper()
    encrypted_message = ""
    for char in message:
        if char == " ":
            encrypted_message += " "
        else:
            new_char = chr(((ord(char) - ord('A') + offset) % 26) + ord('A'))
            encrypted_message += new_char
    return encrypted_message

def main():
    while True:
        message = input("Enter a message to encrypt: ")
        try:
            offset = int(input("Enter an offset (0-26): "))
        except ValueError:
            print("Sorry, we can only process messages wit hletters and spaces, adn the offset must be between 0 and 26")
            continue
        if not validate(message, offset):
            print("Sorry, we can only process messages with letters and soaces, and the offset must be between 0 and 26.")
        else:
            encrypted = encrypt(message, offset)
            print(f"Your secret message is...\n{encrypted}")
        again = input("Do you want to encrypt another message? (Y/N): ").strip().upper()
        if again != 'y':
            print("Closing out...")
            break

if __name__ == "__main__":
    main()