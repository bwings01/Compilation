# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 2c

def rectangle():
    width = int(input("Enter a width: "))
    height = int(input("Enter a height: "))
    perimeter = 2 * (height + width)
    area = (height * width)
    print(f"The area is {area}")
    print(f"The perimeter is {perimeter}")
    return

if __name__ == "__main__":
    rectangle()