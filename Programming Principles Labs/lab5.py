# Program Name: Lab5.py
# Course: IT1114/Section W03
# Student Name: Braeden Wings
# Assignment Number: Lab 5
# Due Date: 02/23/2025
# Purpose: user inputs a starting number and end number and find all the prime numbers between those numbers including the starting number and end number
# I used my knowledge of the python, what I've learned in my IT1114 class and from my Lab, as well as what I've learned from kaggle and other outside resources. Since I used Intellij's pycharm to do my coding, I've also gone and made sure that the code works in IDLE before I submitted.

# function for calculating prime numbers
def is_prime(num):
    # check if number is less than two and also if it equals 1
    if num < 2:
        return True if num == 1 else False
    # loops through numbers from 2 to the square root of the number to check its divisibility
    for i in range(2, int(num ** 0.5) + 1):
        # if num is divisible by any of these numbers then it won't be considered a prime number
        if num % i == 0:
            return False
    # if no divisions other than 1 and the number was found then the number will return a prime number
    return True

# function to find the prime numbers in the inputted range by the user
def calc():
    # user input
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    # validates the range so that the starting number is less than or equal to the ending number
    if start > end:
        print("Starting number should be less than or equal to the ending number.")
        return
    # list for finding all the primes in the range from start to end
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    # if the list of primes is not empty then it will print the primes found in the range
    if primes:
        print(f"{primes}")
    # if no primes were found then it will say so
    else:
        print(f"No prime numbers found between {start} and {end}.")
# block to run the code
if __name__ == "__main__":
    calc()
