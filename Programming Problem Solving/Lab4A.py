# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 4a

def grade():
    gradescore = float(input(f"Enter your grade: "))
    if 97 < gradescore <= 100:
        print("Letter grade is: A+")
    elif 94 < gradescore <= 97:
        print("Letter grade is: A")
    elif 91 < gradescore <= 94:
        print("Letter grade is: A-")
    elif 88 < gradescore <= 91:
        print("Letter grade is: B+")
    elif 85 < gradescore <= 88:
        print("Letter grade is: B")
    elif 82 < gradescore <= 85:
        print("Letter grade is: B-")
    elif 79 < gradescore <= 82:
        print("Letter grade is: C+")
    elif 76 < gradescore <= 79:
        print("Letter grade is: C")
    elif 73 < gradescore <= 76:
        print("Letter grade is: C-")
    elif 70 < gradescore <= 73:
        print("Letter grade is: D+")
    elif 67 < gradescore <= 70:
        print("Letter grade is: D")
    elif 64 < gradescore <= 67:
        print("Letter grade is: D-")
    elif 0 <= gradescore <= 64:
        print("Letter grade is: F")
    else:
        print("Invalid grade entered.")
    return

if __name__ == '__main__':
    grade()