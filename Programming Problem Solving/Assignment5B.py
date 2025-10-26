# importing random for the treasure
import random

# defining width and height of board
width = int(input("Enter the width of the grid: "))
height = int(input("Enter the height of the grid: "))
# getting the board and undiscovered treasure set up for the game
board = []
undiscoveredTreasure = 0 # relied on to tell when the game will end

# makes the nested list row within the board to make the grid
for _ in range(height):
    row = []
    # laying out the Os and Ts in the grid 
    for _ in range(width):
        if random.random() >= 0.7:
            row.append("T")
            undiscoveredTreasure += 1
        else:
            row.append("O")
    # add the new row list to the board list
    board.append(row)
print("Number of treasures hidden: ",undiscoveredTreasure)

# while loop to start the game and take user input to find the treasure
while undiscoveredTreasure > 0:
    try:
        # -1 to show the index numbers after 0 (2 = 1, 3 = 2, etc.)
        rowguess = int(input(f"Enter the row number (0-{height-1}): "))
        columnguess = int(input(f"Enter the column number (0-{width-1}): "))
    except ValueError:
        print("Enter numbers only.")

    # if statement to find if the guesses were correct
    if board[rowguess][columnguess] == "T":
        print("Congratulations! You found a treasure!")
        board[rowguess][columnguess] = "X"
        undiscoveredTreasure -= 1
        # prints board when a treasure is found showing only X's and O's
        for row in board:
            display_row = ["X" if cell == "X" else "O" for cell in row]
            print(' '.join(display_row))
        print()
    
    elif board[rowguess][columnguess] == "X":
        print("You already found this treasure.")

    else:
        print("No tresure here, try again!")

# final message and showing of the complete board at the end of the game
print("Congratulations! You've found all the treasures!")
for row in board:
    print(' '.join(row))
    