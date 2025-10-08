# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 3b

def gpa_calculator():
    course1 = int(input("Course 1 hours: "))
    course1grade = int(input("Grade for course 1: "))
    course2 = int(input("Course 2 hours: "))
    course2grade = int(input("Grade for course 2: "))
    course3 = int(input("Course 3 hours: "))
    course3grade = int(input("Grade for course 3: "))
    course4 = int(input("Course 4 hours: "))
    course4grade = int(input("Grade for course 4: "))

    total_hours = course1 + course2 + course3 + course4
    total_quality_points = (course1*course1grade) + (course2*course2grade) + (course3*course3grade) + (course4*course4grade)
    gpa = total_quality_points / total_hours
    print(f"Total hours: {total_hours}")
    print(f"Total quality points: {total_quality_points}")
    print(f"Your GPA for this semester is {float(round(gpa, 2))}")
    return

if __name__ == "__main__":
    gpa_calculator()