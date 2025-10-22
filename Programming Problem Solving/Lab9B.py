accounts = {}

def usrAuth():
    while True:
        choice = input("Choose and option\n1 - Login\n2 - Register\nE - Exit\n")
        if choice == '1':
            print("[Login]")
            username = input("Username: ")
            password = input("Password: ")
            if username in accounts and accounts[username] == password:
                print("Success!")
                acntMenu(accounts, username)
            else:
                print("Incorrect username/password")
        if choice == '2':
            print("[Register]")
            username = input("Username: ")
            password = input("Password: ")
            accounts[username] = password
            print("User succesfully added!")
        if choice == 'E':
            print("Terminating...")
            break

def acntMenu(accounts, username):
    while True:
        choice = input("Choose an option\n3 - Change password\n4 - Logout\nE - Exit\n")
        if choice == '3':
            print("[Changin password]")
            new_pass = input("Password: ")
            accounts[username] = new_pass
        if choice == '4':
            print("Logging out...")
            return
        if choice == 'E':
            print("Terminating...")
            break

if __name__ == "__main__":
    usrAuth()