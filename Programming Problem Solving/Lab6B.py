# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 6b

import random

def guessing_game():
    print("Guess the number I am thinking!")
    random_number = random.randint(1, 100)
    while True:
        user_input = int(input("Enter any number between 1 and 100: "))
        if user_input == random_number:
            print(f"Correct! I was thinking of {random_number}")
            break
        elif user_input > random_number:
            print("Too high!")
        else:
            print("Too low!")

if __name__ == '__main__':
    guessing_game()