# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 4c

def triangle():
    firstside = int(input("Enter the first side of the triangle: "))
    secondside = int(input("Enter the second side of the triangle: "))
    thirdside = int(input("Enter the third side of the triangle: "))

    if firstside <= 0 or secondside <= 0 or thirdside <= 0:
        print("Invalid input. All sides must be greater than 0.")
    elif firstside + secondside <= thirdside or firstside + thirdside <= secondside or secondside + thirdside <= firstside:
        print("The sides do not form a valid triangle.")
    elif firstside == secondside == thirdside:
        print("The triangle is an equilateral triangle.")
    elif firstside == secondside or firstside == thirdside or secondside == thirdside:
        print("The triangle is an isosceles triangle.")
    else:
        print("The triangle is a scalene triangle.")
    return

if __name__ == "__main__":
    triangle()