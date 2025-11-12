def input_int():
    print("[My Integer Collection]")
    # initalize list
    numList = []
    # while loop
    while True:
        # checking if the amount of integers entered by the user reaches the 10 entry limit
        if len(numList) >= 10:
            break
        # getting user input
        try:
            value = int(input("Enter an integer: "))
            numList.append(value)
        # throw an exception if a non integer is entered
        except ValueError:
            print("Please enter a whole number (no decimals), try again.")
    # printing in proper format
    print("These are the numbers you entered: ")
    # for each spot in the list and the value assigned to it, change the spot to start at 0 and count up for the next entry until there is no more ("0. 1, 1. 2, 2. 3, ...")
    for i, val in enumerate(numList, start=0):
        print(f"{i}. {val}")


if __name__ == "__main__":
    input_int()