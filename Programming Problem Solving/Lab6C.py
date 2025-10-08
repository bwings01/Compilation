# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 6c

def pyramid():
    rows = int(input("Enter number for Rows or 0 to quit: "))
    for i in range(1, rows+1):
        print(" " * (rows - i), end="")
        for j in range(i, 0, -1):
            print(j, end="")
        for j in range(2, i + 1):
            print(j, end="")
        print()

if __name__ == '__main__':
    pyramid()