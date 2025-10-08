# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 3c

def sandwiches():
    small_sand = int(input("Enter the number of small sandwiches: "))
    medium_sand = int(input("Enter the number of medium sandwiches: "))
    large_sand = int(input("Enter the number of large sandwiches: "))
    xl_sand = int(input("Enter the number of extra-large sandwiches: "))

    print(f"You've entered {small_sand} small sandwiches.\n You've entered {medium_sand} medium sandwiches.\n You've entered {large_sand} large sandwiches.\n You've entered {xl_sand} extra-large sandwiches.")

    cooking_time = ((small_sand*30) + (medium_sand*60) + (large_sand*75) + (xl_sand*135))

    minutes = cooking_time // 60
    seconds = cooking_time % 60
    print(f"Total cooking time is {minutes} minutes and {seconds} seconds.")
    return

if __name__ == "__main__":
    sandwiches()