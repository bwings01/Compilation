# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 5a

def number_loop():
    print("Please enter 10 numbers and this program will display the largest.")
    numbers = []
    for i in range(10):
        num = int(input(f"Please enter number {i+1}: "))
        numbers.append(num)

    largest_number = max(numbers)
    print(f"\nThe largest number was {largest_number}")

if __name__ == "__main__":
    number_loop()