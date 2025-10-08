# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 6a

def calculator():
    print("Multiplication and Exponent Calculator")
    user_input = int(input(f"Choose option 1 for Multiplication\nChoose option 2 for Exponentiation\nChoose option 3 to exit"))
    match user_input:
        case 1:
            operand1 = int(input("Enter an operand: "))
            operand2 = int(input("Enter the other operand: "))
            result = 0
            for i in range(operand2):
                result += operand1
            print(f"{operand1} x {operand2} = {result}")
        case 2:
            base = int(input("Enter the base: "))
            exponent = int(input("Enter the exponent: "))
            result = 1
            for i in range(exponent):
                result *= base
            print(f"{base}^({exponent}) = {result}")
        case 3:
            print("Closing the Calculator...")
        case _:
            print("Invalid Choice")
    return

if __name__ == "__main__":
    calculator()