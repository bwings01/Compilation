# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 4b

from unittest import case

def menu():
    print("Welcome!")
    user_number = float(input("Please input a number:"))
    menu_answer = int(input("What would you like to do with this number:\n0) Get the additive inverse of the number\n1) Get the reciprocal of the number\n2) Square the number\n3) Cube the number\n4) Exit the program\n"))
    match menu_answer:
        case 0:
            num = -1 * user_number
            print(f"The additive inverse of {user_number} is {round(num, 3)}")
        case 1:
            try:
                num = 1 / user_number
                print(f"The reciprocal of {user_number} is {round(num, 3)}")
            except ZeroDivisionError:
                print("Cannot divide by 0!")
        case 2:
            num = user_number * user_number
            print(f"The square of {user_number} is {round(num, 3)}")
        case 3:
            num = (user_number * user_number) * user_number
            print(f"The cube of {user_number} is {round(num, 3)}")
        case 4:
            print("Thank you, goodbye!")
        case _:
            print("Invalid option!")
    return

if __name__ == "__main__":
    menu()