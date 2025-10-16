def mailing_list():
    emails = []
    while True:
        print("[Mailing list]\n")
        print("1 - Add email\n2 - Delete email\n3 - List all emails\n4 - Quit\n")
        choice = int(input("Make your selection: "))
        if choice == 1:
            email = input("Enter the email to be added: ")
            emails.append(email)
            print("Email added to mailing list")
        elif choice == 2:
            deleteEmail = input("Enter Email to be deleted: ")
            for i in emails:
                if deleteEmail in emails:
                    emails.remove(deleteEmail)
                    print("Email deleted from mailing list")
                else:
                    print("Email not found in mailing list")
        elif choice == 3:
            if emails:
                print("Emails in mailing list: ")
                for email in emails:
                    print(email)
                else:
                    print("Mailing list is empty")
        elif choice == 4:
            print("Shutting down...")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    mailing_list()
