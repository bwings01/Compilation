# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 1c

# Program Lab1C.py
# Demonstrate the use of the input function to read numeric data.
# Calculates fuel efficiency based on values entered by the user.
miles = int(input ("Enter the number of miles: "))
gallons = int(input ("Enter the gallons of fuel used: "))
mpg = miles/gallons
print ("Miles Per Gallon: " + str (mpg))