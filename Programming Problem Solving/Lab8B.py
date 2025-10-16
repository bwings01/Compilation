def friendList():
    # a list which will contain tuples
    friends = []
    while True:
        print("\n[Friend List]\n")
        print("1 - Add friend\n2 - List friends\n3 - Quit")
        choice = int(input("Make your selection: "))
        if choice == 1:
            friendName = input("Enter your friend's name: ")
            friendAge = int(input("Enter your friend's age: "))
            friends.append((friendName, friendAge))
        elif choice == 2:
            for friend in friends:
                print(f"Name: {friend[0]}, Age: {friend[1]}")
        elif choice == 3:
            print("Shutting down...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    friendList()
