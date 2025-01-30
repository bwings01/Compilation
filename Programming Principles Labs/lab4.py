# Program name: Lab4.py
# Course: IT1114/Section W03
# Student Name: Braeden Wings
# Assignment Number: Lab 3
# Due Date: 02/09/2025
# Purpose: A program to determine the cost of a resort vacation including the cost of booking, dining, and special excursions
# I used my knowledge of the python, what I've learned in my IT1114 class and from my Lab, as well as what I've learned from kaggle and other outside resources. Since I used Intellij's pycharm to do my coding, I've also gone and made sure that the code works in IDLE before I submitted.

# function for calculating room cost per night
def room_cost():
    # defining room options
    two_queen = 375
    one_king = 350
    queen_suite = 525
    king_suite = 475
    # variables to ask how many nights and how many people are staying on the vacation
    nights = int(input("Enter the number of nights staying: "))
    # added to a global statement below so that it could be used outside the function
    global people_amount
    people_amount = int(input("Enter the number of people going on the vacation: "))
    # while loop to see the decision of which room the customer would like to stay in
    while True:
        try:
            room_type = int(input("Which room type would you like? (1: Two Queen Beds, 2: One King Bed, 3: Queen Suite, 4: King Suite): "))
            if room_type == 1:
                return two_queen * nights
            elif room_type == 2:
                return one_king * nights
            elif room_type == 3:
                return queen_suite * nights
            elif room_type == 4:
                return king_suite * nights
            else:
                print("Invalid input! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# global statement to carry the amount of nights and people outside the room_cost function
global people_amount

# function for calculating meal cost
def meal_cost():
    # defining meal options
    brunch = 25
    dinner = 75
    # while loop to calculate the cost of brunch and dinner that is entered with gratuity on top
    while True:
        try:
            # user input for the number of brunches and dinners they need
            num_brunch = int(input("Enter the number of brunch meals: "))
            num_dinner = int(input("Enter the number of dinner meals: "))
            # if statement to calculate the total based on the user input above
            if num_brunch >= 0 and num_dinner >= 0:
                total_meal = ((num_brunch * brunch) + (num_dinner * dinner))
                # calculating gratuity
                gratuity = total_meal * 0.15
                # will calculate the total cost of the meals by adding the total_meal variable and the gratuity variable above
                total_meal_cost = gratuity + total_meal
                # returns the total cost of all the meals selected
                return total_meal_cost
            else:
                print("Meal counts cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

# function for calculating excursion cost
def excursion_cost():
    # necessary for the people_amount variable to work inside this function
    global people_amount
    # defining excursion options and their costs
    excursions = {
        "Picnic Excursion": 50,
        "Snorkeling Excursion": 25 * people_amount,
        "Guided Hike Excursion": 17 * people_amount,
        "Boat Dinner Excursion": 200
    }
    # initialize the total excursion cost
    total_excursion_cost = 0

    # Iterate through each excursion and ask the user if they want it
    for excursion_name, excursion_cost in excursions.items():
        while True:
            try:
                # Ask for user input and validate the response
                response = input(f"Would you like the {excursion_name}? (y/n): ").strip().lower()
                if response == 'y':
                    total_excursion_cost += excursion_cost
                    break
                elif response == 'n':
                    break
                else:
                    print("Invalid input! Please enter 'y' for yes or 'n' for no.")
            except ValueError:
                print("Invalid input! Please try again.")

    # Return the total cost of all selected excursions
    return total_excursion_cost

# function for calculating the total vacation cost and list out each price like in the example
def vacation_cost():
    # will call the room_cost function first and make it equal the room_total_cost variable
    room_total_cost = room_cost()
    # will call the meal cost function second and make it equal the meal_total_cost variable
    meal_total_cost = meal_cost()
    # will call the excursion_cost function last and make it equal the excursion_total_cost variable
    excursion_total_cost = excursion_cost()
    # calculation of the total vacation cost
    total_vacation_cost = room_total_cost + meal_total_cost + excursion_total_cost
    # will print each of the required costs from the sample
    print("Room cost: $", room_total_cost)
    print("Meal cost: $", meal_total_cost)
    print("Excursion cost: $", excursion_total_cost)
    print("Total vacation cost: $", total_vacation_cost)

# a block to call the vacation cost function on startup
if __name__ == "__main__":
    vacation_cost()
